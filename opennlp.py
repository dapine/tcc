import bs4
import sys
import random
from bs4 import BeautifulSoup
from harem import *

stdout = sys.stdout

# filename = 'harem.xml'
opcao = sys.argv[1]
filename = sys.argv[2]

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

def print_ps(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None and '|' in t.categoria:
                    cat = t.categoria.split('|')[0]

                print(' <START:{}> {} <END> '.format(cat, t.texto), end='')
            else:
                print(t.texto, end='')

def print_file(paragrafos, arquivo):
    with open(arquivo, 'w') as f:
        sys.stdout = f
        print_ps(paragrafos)
        sys.stdout = stdout

def treino_teste(paragrafos, n):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]
    teste = paragrafos[n+1:len(paragrafos)]

    print_file(treino, 'tmp/opennlp/harem-100.train')
    print_file(teste, 'tmp/opennlp/harem-100.test')

def completo(paragrafos, n, saida):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]

    print_file(treino, saida)

paragrafos = todos_paragrafos(documentos)

# pt-br = 569
# pt-pt = 3304

if opcao == 'holdout':
    treino_teste(paragrafos, 2000)
elif opcao == 'ptbr':
    completo(paragrafos, 569, 'tmp/opennlp/ptbr.train')
elif opcao == 'ptpt':
    completo(paragrafos, 569, 'tmp/opennlp/ptpt.train')
elif opcao == 'completo':
    completo(paragrafos, 569, 'tmp/opennlp/harem.train')
elif opcao == 'completo-test':
    completo(paragrafos, 569, 'tmp/opennlp/harem.test')
