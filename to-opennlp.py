import bs4
import nltk
from bs4 import BeautifulSoup

f = open('harem-utf8.xml', 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

def pp(p):
    if type(p) is bs4.element.Tag:
        if p.name == 'em':
            categ = p.get('categ')
            if categ is None:
                print(p.string, end='')
            else:
                if '|' in categ:
                    categ = categ.split('|')[0]

                print(' <START:{0}> {1} <END> '.format(categ, p.string), end='')
        else:
            for x in p.contents:
                pp(x)
    else:
        tokens = nltk.word_tokenize(p.string)
        print(' '.join(tokens), end='')
        # print(p.string, end='')

for doc in docs:
    for p in doc.contents:
        pp(p)
        print()
