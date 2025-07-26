import requests
from bs4 import BeautifulSoup

def removeExtraWhitespace(text_str):
    if not text_str:
        return
    text_str = text_str.replace('\n', ' ')
    while '  ' in text_str:
        text_str = text_str.replace('  ', ' ')
    while text_str[0] == ' ':
        text_str = text_str[1:]
    
    return text_str
    
def tabSpace():
    return ' '*4

def findParent(meaning_list, parent_id):
    for prev_meaning in meaning_list:
        if (parent_id == prev_meaning['id']):
            return prev_meaning
            
class Parser:
    def __init__(self):
        pass

    def process(self, vocabulary):
        link = "https://www.dwds.de/wb/"+vocabulary
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")
        self.main_soup = soup.find('main')
        self.word = vocabulary
        self.processGarammer()
        self.processFrequency()
        self.processMeanings()


    def processGarammer(self):
        gram_soup = self.main_soup.find('div', {'class':'dwdswb-ft-block'})
        gram_text = gram_soup.find('span',{'class':'dwdswb-ft-blocktext'}).text
        gram_text = gram_text.replace('·','|')
        gram_text = gram_text.replace('Maskulinum','der')
        gram_text = gram_text.replace('Femininum','die')
        gram_text = gram_text.replace('Neutrum','das')
        self.grammar = gram_text
            
    def processFrequency(self):
        self.frequency = len(self.main_soup.find_all('div', {'class':'word-frequency-active'}))

    def processMeanings(self):
        self.meanings = []
        meanings_soup = self.main_soup.find_all('div', {'class':'dwdswb-lesart'})
        for cur_meaning_soup in meanings_soup:
            cur_meaning = {}

            # Labels
            cur_meaning = self.processLabels(cur_meaning_soup, cur_meaning)

            # Definition
            cur_meaning = self.processDefinitions(cur_meaning_soup, cur_meaning)
            
            # Kollokationen
            cur_meaning = self.processCollocations(cur_meaning_soup, cur_meaning)
            
            # Examples
            cur_meaning = self.processExamples(cur_meaning_soup, cur_meaning)

            # Add to list
            self.meanings.append(cur_meaning)
            
    def processLabels(self, meaning_soup, ret_meaning_dict):
        ret_meaning_dict['id'] = meaning_soup['id']
        parent_id = ret_meaning_dict['id'][:-2]

        parent_meaning = findParent(self.meanings, parent_id)
        if parent_meaning is not None:
            ret_meaning_dict['label_parent'] = parent_meaning['label_base']

        id_segments = meaning_soup['id'].split('-')
        ret_meaning_dict['indent'] = len(id_segments)-3

        n_label = meaning_soup.find('div' ,{'class':'dwdswb-lesart-n'}).text
        if n_label == '':
            n_label = '●'
            
        base_label = n_label.replace('.','')
        base_label = base_label.replace(')','')

        ret_meaning_dict['label_base'] = base_label
        ret_meaning_dict['label_definition'] = n_label
        if 'label_parent' in ret_meaning_dict:
            ret_meaning_dict['label_full'] = parent_meaning['label_full']+'.'+base_label
        else:
            ret_meaning_dict['label_full'] = base_label
        ret_meaning_dict['label_example'] = '['+ret_meaning_dict['label_full']+'] '

        return ret_meaning_dict

    def processDefinitions(self, meaning_soup, ret_meaning_dict):
        content_soup = meaning_soup.find('div',{'class':'dwdswb-lesart-content'})
        def_soup = content_soup.find('div', {'class':'dwdswb-lesart-def'})

        definition_text = ""

        diasys_soup = def_soup.find('span', {'class':'dwdswb-diasystematik'})
        if diasys_soup is not None:
            definition_text = '['+diasys_soup.text+'] '+definition_text

        freq_soup = def_soup.find('span', {'class':'dwdswb-frequenzangabe'})
        if freq_soup is not None:
            definition_text = '['+freq_soup.text+'] '+definition_text
            
        syntac_soup = def_soup.find('span', {'class':'dwdswb-syntagmatik'})
        if syntac_soup is not None:
            definition_text = definition_text+' '+syntac_soup.text
            
        specification_soup = def_soup.find('span', {'class':'dwdswb-definition-spezifizierung'})
        if specification_soup is not None:
            definition_text = definition_text+' <'+specification_soup.text+'>'

        definition_list = def_soup.find_all('span', {'class':'dwdswb-definition'})
        if definition_list:
            cur_text = ''
            for definition_soup in definition_list:
                cur_text += definition_soup.text
            definition_text = definition_text+' '+cur_text

        ftla_soup = content_soup.find('div', {'class':'dwdswb-ft-la'}, recursive=False)
        if ftla_soup is not None:
            definition_text = definition_text+' {'+ftla_soup.text+'}'

        verweise_soup = content_soup.find('span', {'class':'dwdswb-verweis'}, recursive=False)
        if verweise_soup is not None:
            definition_text = definition_text+' ('+verweise_soup.text+')'
        else:
            verweise_soup = content_soup.find('div', {'class':'dwdswb-verweise'}, recursive=False)
            if verweise_soup is not None:
                definition_text = definition_text+' ('+verweise_soup.text+')'

        phrasem_soup = content_soup.find('div', {'class':'dwdswb-phraseme'}, recursive=False)
        if phrasem_soup is not None:
            definition_text = definition_text+' '+phrasem_soup.text

        definition_text = definition_text.replace('⟩', '⟩ ')
        definition_text = removeExtraWhitespace(definition_text)
        if definition_text is None:
            definition_text = '...'
        ret_meaning_dict['definition'] = definition_text
        return ret_meaning_dict

    def processCollocations(self, meaning_soup, ret_meaning_dict):
        content_soup = meaning_soup.find('div',{'class':'dwdswb-lesart-content'})
        kollokationen_soup = content_soup.find('div', {'class':'dwdswb-kollokationen'}, recursive=False)
        if kollokationen_soup is not None:
            koll_list = kollokationen_soup.find_all('div', {'class':'dwdswb-kollokation'})
            if len(koll_list) > 0:
                ret_meaning_dict['collocations'] = []
            for koll in koll_list:
                relation_text = koll.find('span', {'class':'dwdswb-relation'}).text
                relation_text = relation_text.replace(': ','')
                beleg_soup_list = koll.find_all('span', {'class':'dwdswb-belegtext'})
                beleg_list = []
                for beleg_soup in beleg_soup_list:
                    beleg_list.append(beleg_soup.text)
                beleg_text = '; '.join(beleg_list)
                
                koll_text = '{'+relation_text+'}\t'+beleg_text
                
                koll_text = removeExtraWhitespace(koll_text)
                ret_meaning_dict['collocations'].append(koll_text)
        return ret_meaning_dict

    def processExamples(self, meaning_soup, ret_meaning_dict):
        content_soup = meaning_soup.find('div',{'class':'dwdswb-lesart-content'})
        example_soup = content_soup.find('div', {'class':'dwdswb-verwendungsbeispiele'}, recursive=False)
        if example_soup is not None:
            example_komp_list = example_soup.find_all('div', {'class':'dwdswb-kompetenzbeispiel'})
            example_belg_list = example_soup.find_all('div', {'class':'dwdswb-beleg'})
            example_list = example_komp_list + example_belg_list
            if len(example_list) > 0:
                ret_meaning_dict['examples'] = []
            for example_soup in example_list:
                example_text = ""
                
                example_diasys_soup = example_soup.find('span', {'class':'dwdswb-diasystematik'})
                if example_diasys_soup is not None:
                    example_text = '['+example_diasys_soup.text+'] '+example_text
                example_text = example_text+example_soup.find('span', {'class':'dwdswb-belegtext'}).text
                
                example_text = removeExtraWhitespace(example_text)
                ret_meaning_dict['examples'].append(example_text)
        return ret_meaning_dict
    
    def getGrammar(self):
        return self.grammar+'\n'

    def getFrequency(self):
        return 'h'+str(self.frequency)+'\n'

    def getDefinitions(self):
        ret_string = ''
        for meaning in self.meanings:
            ret_string += tabSpace()*meaning['indent']+meaning['label_definition'] + ' ' + meaning['definition']+'\n'
        return ret_string

    def getExamples(self, example_number):
        ret_string = ''
        for meaning in self.meanings:
            if 'collocations' in meaning:
                ret_string += meaning['label_example']+'Kollokationen:\n'
                for kol in meaning['collocations']:
                    ret_string += tabSpace()+kol+'\n'

            if 'examples' in meaning:
                for jj, example in enumerate(meaning['examples']):
                    if jj == example_number:
                        break;
                    ret_string += meaning['label_example']+example+'\n'

            if 'collocations' in meaning:
                ret_string += '\n'
        return ret_string
