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

def todos_paragrafos(docs):
    par = []
    for doc in docs:
        for p in doc.paragrafos:
            par.append(p)

        par.append('--newdoc--')

    return par

def print_ps(paragrafos):
    for p in paragrafos:
        if p == '--newdoc--':
            print()
        else:
            for t in p.lista:
                if t.t == 'em':
                    cat = t.categoria
                    if t.categoria != None and '|' in t.categoria:
                        cat = t.categoria.split('|')[0]

                    tokens = t.texto.split()

                    for i, tok in enumerate(tokens):
                        if i == 0:
                            print('{0} -X- O B-{1}'.format(tok, cat))
                        else:
                            print('{0} -X- O I-{1}'.format(tok, cat))
                else:
                    tokens = t.texto.split()

                    for tok in tokens:
                        print('{0} -X- O {1}'.format(tok, 'O'))

def print_file(paragrafos, arquivo):
    with open(arquivo, 'w') as f:
        sys.stdout = f
        print_ps(paragrafos)
        sys.stdout = stdout

def treino_teste(paragrafos, n):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]
    teste = paragrafos[n+1:len(paragrafos)]

    print_file(treino, 'tmp/spacy/harem-100.train')
    print_file(teste, 'tmp/spacy/harem-100-test.test')

paragrafos = todos_paragrafos(documentos)

def completo(paragrafos, n, saida):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]

    print_file(treino, saida)

# pt-br = 569
# pt-pt = 3304

if opcao == 'holdout':
    treino_teste(paragrafos, 2000)
elif opcao == 'ptbr':
    completo(paragrafos, 569, 'tmp/spacy/ptbr.train')
elif opcao == 'ptpt':
    completo(paragrafos, 569, 'tmp/spacy/ptpt.train')
elif opcao == 'completo':
    completo(paragrafos, 569, 'tmp/spacy/harem.train')
elif opcao == 'completo-test':
    completo(paragrafos, 569, 'tmp/spacy/harem-test.test')

