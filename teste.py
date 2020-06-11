import bs4
import nltk
import sys
from bs4 import BeautifulSoup
from unicodedata import normalize

filename = 'harem-utf-sem-omitido-alt.xml'
# filename = sys.argv[1]

f = open(filename, 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

class Doc:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag and tag.name == 'doc':
            self.paragrafos = []
            for p in tag.contents:
                self.paragrafos.append(P(p))

class P:
    def __init__(self, tag):
        self.lista = []
        if type(tag) is bs4.element.Tag and tag.name == 'p':
            for e in tag.contents:
                self.lista.append(Em(e))

class Em:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag:
            self.categoria = tag.get('categ')
            self.texto = tag.string.strip()
            self.id = tag.get('id')
            self.tipo = tag.get('tipo')
            self.t = 'em'
        else:
            self.categoria = ''
            self.texto = tag.string.strip()
            self.id = ''
            self.tipo = ''
            self.t = 'plain_text'

documentos = []

for doc in docs:
    documentos.append(Doc(doc))

# for doc in documentos:
#     for p in doc.paragrafos:
#         for t in p.lista:
#             if t.t == 'em':
#                 print('<START:{}> {} <END>'.format(t.categoria, t.texto), end='')
#             else:
#                 print(t.texto, end='')

def todos_paragrafos(docs):
    par = []
    for doc in docs:
        for p in doc.paragrafos:
            par.append(p)

    return par

paragrafos = todos_paragrafos(documentos)

# 2773
p_min = 0
p_max = 2000

limite_p = paragrafos[p_min:p_max]
c = 0

for p in limite_p:
    for t in p.lista:
        if t.t == 'em':
            cat = t.categoria
            if t.categoria != None and '|' in t.categoria:
                cat = t.categoria.split('|')[0]

            print(' <START:{}> {} <END> '.format(cat, t.texto), end='')
        else:
            print(t.texto, end='')
    if c % 2 >= 1:
        print()

    c += 1
