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

def todos_paragrafos2(docs):
    par = []
    for doc in docs:
        for p in doc.paragrafos:
            # retornar tupla
            # par.append((doc.id, p))

    return par

paragrafos = todos_paragrafos2(documentos)

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
