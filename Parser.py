# This Python file uses the following encoding: utf-8
import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self, ):
        pass


    def load(self, vocabulary):
        link = "https://www.dwds.de/wb/"+vocabulary
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        self.main_soup = soup.find('main')
        self.vocabulary = vocabulary

    def getGrammar(self):
        gram_soup = self.main_soup.find('div', {'class':'dwdswb-ft-block'})

        gram_text = gram_soup.find('span',{'class':'dwdswb-ft-blocktext'}).text
        gram_text = gram_text.replace('·','|')
        gram_text = gram_text.replace('Maskulinum','der')
        gram_text = gram_text.replace('Femininum','die')
        gram_text = gram_text.replace('Neutrum','das')
        return gram_text


