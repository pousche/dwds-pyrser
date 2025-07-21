# This Python file uses the following encoding: utf-8
import requests
from bs4 import BeautifulSoup

def remove_extra_whitespace(text_str):
    if not text_str:
        return
    text_str = text_str.replace('\n', ' ')
    while '  ' in text_str:
        text_str = text_str.replace('  ', ' ')

    while text_str and text_str[0] == ' ':
        text_str = text_str[1:]

    return text_str

def tab_space():
    return ' '*4

def find_parent(meaning_list, parent_id):
    for prev_meaning in meaning_list:
        if (parent_id == prev_meaning['id']):
            return prev_meaning

class Parser:
    def __init__(self, ):
        pass


    def load(self, vocabulary):
        link = "https://www.dwds.de/wb/"+vocabulary
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        self.main_soup = soup.find('main')
        self.vocabulary = vocabulary
        self.loadMeanings()

    def getGrammar(self):
        gram_soup = self.main_soup.find('div', {'class':'dwdswb-ft-block'})

        gram_text = gram_soup.find('span',{'class':'dwdswb-ft-blocktext'}).text
        gram_text = gram_text.replace('·','|')
        gram_text = gram_text.replace('Maskulinum','der')
        gram_text = gram_text.replace('Femininum','die')
        gram_text = gram_text.replace('Neutrum','das')
        return gram_text

    def getFrequency(self):
        return len(self.main_soup.find_all('div', {'class':'word-frequency-active'}))

    def loadMeanings(self):
        self.meanings = []

        meanings_soup = self.main_soup.find_all('div', {'class':'dwdswb-lesart'})
        for meaning_soup in meanings_soup:
            meaning = {}

            # Laebls
            meaning['id'] = meaning_soup['id']
            parent_id = meaning['id'][:-2]

            parent_meaning = find_parent(self.meanings, parent_id)
            if parent_meaning is not None:
                meaning['label_parent'] = parent_meaning['label_base']

            id_segments = meaning_soup['id'].split('-')
            label_segments = [id_segments[2]]

            if len(id_segments) > 3:
                sub_id = id_segments[3]
                label_segments.append(chr(96+int(sub_id)))
                if len(id_segments) > 4:
                    sub_sub_id = id_segments[4]
                    label_segments.append(chr(944+int(sub_sub_id)))

            meaning['indent'] = len(label_segments)-1

            n_label = meaning_soup.find('div' ,{'class':'dwdswb-lesart-n'}).text
            if n_label == '':
                n_label = '●'
            base_label = n_label.replace('.','')
            base_label = base_label.replace(')','')
            if len(meaning_soup) < 2:
                meaning['label_base'] = '-'
                meaning['label_definition'] = '-'
                meaning['label_example'] = '[-] '
            else:
                meaning['label_base'] = base_label
                meaning['label_definition'] = n_label
                if 'label_parent' in meaning:
                    meaning['label_full'] = parent_meaning['label_full']+'.'+base_label
                else:
                    meaning['label_full'] = base_label
                meaning['label_example'] = '['+meaning['label_full']+'] '

            n_label = meaning_soup.find('div' ,{'class':'dwdswb-lesart-n'}).text
            base_label = n_label.replace('.','')
            base_label = base_label.replace(')','')

            content_soup = meaning_soup.find('div',{'class':'dwdswb-lesart-content'})

            # Definition
            def_soup = content_soup.find('div', {'class':'dwdswb-lesart-def'})

            definition_text = ""

            diasys_soup = def_soup.find('span', {'class':'dwdswb-diasystematik'})
            if diasys_soup is not None:
                definition_text = '['+diasys_soup.text+'] '+definition_text

            syntac_soup = def_soup.find('span', {'class':'dwdswb-syntagmatik'})
            if syntac_soup is not None:
                definition_text = definition_text+' '+syntac_soup.text

            specification_soup = def_soup.find('span', {'class':'dwdswb-definition-spezifizierung'})
            if specification_soup is not None:
                spec_text = specification_soup.text
                definition_text = definition_text+' <'+spec_text+'>'

            definition_list = def_soup.find_all('span', {'class':'dwdswb-definition'})
            if definition_list:
                cur_text = ''
                for definition_soup in definition_list:
                    cur_text += definition_soup.text
                definition_text = definition_text+' '+cur_text

            ftla_soup = content_soup.find('div', {'class':'dwdswb-ft-la'})
            if ftla_soup is not None:
                definition_text = definition_text+' {'+ftla_soup.text+'}'

            verweise_soup = def_soup.find('span', {'class':'dwdswb-verweise'})
            if verweise_soup is not None:
                definition_text = definition_text+' '+verweise_soup.text


            definition_text = definition_text.replace('⟩', '⟩ ')
            definition_text = remove_extra_whitespace(definition_text)
            if definition_text is None:
                definition_text = '...'
            meaning['definition'] = definition_text

            # Kollokationen
            kollokationen_soup = content_soup.find('div', {'class':'dwdswb-kollokationen'}, recursive=False)
            if kollokationen_soup is not None:
                koll_list = kollokationen_soup.find_all('div', {'class':'dwdswb-kollokation'})
                if len(koll_list) > 0:
                    meaning['collocations'] = []
                for koll in koll_list:
                    relation_text = koll.find('span', {'class':'dwdswb-relation'}).text
                    relation_text = relation_text.replace(': ','')
                    beleg_soup_list = koll.find_all('span', {'class':'dwdswb-belegtext'})
                    beleg_list = []
                    for beleg_soup in beleg_soup_list:
                        beleg_list.append(beleg_soup.text)
                    beleg_text = '; '.join(beleg_list)

                    koll_text = '{'+relation_text+'}\t'+beleg_text

                    koll_text = remove_extra_whitespace(koll_text)
                    meaning['collocations'].append(koll_text)

            # Examples
            example_soup = content_soup.find('div', {'class':'dwdswb-verwendungsbeispiele'}, recursive=False)
            if example_soup is not None:
                example_komp_list = example_soup.find_all('div', {'class':'dwdswb-kompetenzbeispiel'})
                example_belg_list = example_soup.find_all('div', {'class':'dwdswb-beleg'})
                example_list = example_komp_list + example_belg_list
                if len(example_list) > 0:
                    meaning['examples'] = []
                for example_soup in example_list:
                    example_text = ""

                    example_diasys_soup = example_soup.find('span', {'class':'dwdswb-diasystematik'})
                    if example_diasys_soup is not None:
                        example_text = '['+example_diasys_soup.text+'] '+example_text
                    example_text = example_text+example_soup.find('span', {'class':'dwdswb-belegtext'}).text

                    example_text = remove_extra_whitespace(example_text)
                    meaning['examples'].append(example_text)

            # Add to list
            self.meanings.append(meaning)


    def getDefinition(self):
        ret_string = ''
        for meaning in self.meanings:
            ret_string += tab_space()*meaning['indent']+meaning['label_definition'] + ' ' + meaning['definition']+'\n'
        return ret_string

    def getExamples(self, example_number):
        ret_string = ''
        for meaning in self.meanings:
            if 'collocations' in meaning:
                ret_string += meaning['label_example']+'Kollokationen:\n'
                for kol in meaning['collocations']:
                    ret_string += ' '*4+kol+'\n'

            if 'examples' in meaning:
                for jj, example in enumerate(meaning['examples']):
                    if jj == example_number:
                        break;
                    ret_string += meaning['label_example']+example+'\n'

            if 'collocations' in meaning:
                ret_string += '\n'
        return ret_string
