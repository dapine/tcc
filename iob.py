import bs4
import sys
import random
from bs4 import BeautifulSoup
from harem import *

stdout = sys.stdout

filename = sys.argv[1]
opcao = sys.argv[2]
variante = sys.argv[3]
porcentagem = sys.argv[4]

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

def print_ps_sem_acento(paragrafos):
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
                            print('{0} -X- O B-{1}'.format(remover_acentuacao(tok), cat))
                        else:
                            print('{0} -X- O I-{1}'.format(remover_acentuacao(tok), cat))
                else:
                    tokens = t.texto.split()

                    for tok in tokens:
                        print('{0} -X- O {1}'.format(remover_acentuacao(tok), 'O'))

paragrafos = todos_paragrafos(documentos)

cli(paragrafos, opcao, variante, 'tmp/spacy/', print_ps, stdout, porcentagem)
