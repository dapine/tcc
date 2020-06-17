import bs4
import sys
from bs4 import BeautifulSoup
from harem import *

filename = 'harem.xml'
# filename = sys.argv[1]

f = open(filename, 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

documentos = []

for doc in docs:
    documentos.append(Doc(doc))

def todos_paragrafos(docs):
    par = []
    for doc in docs:
        for p in doc.paragrafos:
            par.append(p)

    return par

paragrafos = todos_paragrafos(documentos)

# 2773
p_min = 0
p_max = 772

limite_p = paragrafos[p_min:p_max]

for p in limite_p:
    for t in p.lista:
        if t.t == 'em':
            cat = t.categoria
            if t.categoria != None and '|' in t.categoria:
                cat = t.categoria.split('|')[0]

            tokens = t.texto.split()

            for tok in tokens:
                print('{}\t{}'.format(tok, cat))
        else:
            tokens = t.texto.split()

            for tok in tokens:
                print('{}\t{}'.format(tok, 'O'))
