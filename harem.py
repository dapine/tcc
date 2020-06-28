import bs4
from bs4 import BeautifulSoup
import random
import sys

class Doc:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag and tag.name == 'doc':
            self.paragrafos = []
            self.id = tag.get('id')
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

def get_docs(f):
    soup = BeautifulSoup(f, 'lxml')
    docs = soup.find_all('doc')

    documentos = []

    for doc in docs:
        documentos.append(Doc(doc))

    return documentos

def todos_paragrafos(docs):
    par = []
    for doc in docs:
        for p in doc.paragrafos:
            par.append(p)

    return par

def print_file(paragrafos, arquivo, print_ps, stdout):
    with open(arquivo, 'w') as f:
        sys.stdout = f
        print_ps(paragrafos)
        sys.stdout = stdout

def treino_teste(paragrafos, n, out_treino, out_teste, print_f, stdout):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]
    teste = paragrafos[n+1:len(paragrafos)]

    print_file(treino, out_treino, print_f, stdout)
    print_file(teste, out_teste, print_f, stdout)

def completo_mix(paragrafos, n, out_treino, out_teste, print_f, stdout):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]
    teste = paragrafos[n+1:n+n]

    print_file(treino, out_treino, print_f, stdout)
    print_file(teste, out_teste, print_f, stdout)

def completo(paragrafos, n, saida, print_f, stdout):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]

    print_file(treino, saida, print_f, stdout)

def cli(paragrafos, opcao, variante, caminho, print_f, stdout, porcentagem=0.7):
    if opcao == 'holdout':
        p = float(porcentagem)
        if variante == 'ptbr':
            treino_teste(paragrafos, round(len(paragrafos)*p), caminho+'ptbr-holdout.train', caminho+'ptbr-holdout.test', print_f, stdout)
        elif variante == 'ptpt':
            treino_teste(paragrafos, round(len(paragrafos)*p), caminho+'ptpt-holdout.train', caminho+'ptpt-holdout.test', print_f, stdout)
        else:
            treino_teste(paragrafos, round(len(paragrafos)*p), caminho+'harem.train', caminho+'harem.test', print_f, stdout)
    elif opcao == 'completo':
        if variante == 'ptbr':
            completo(paragrafos, 569, caminho+'ptbr.train', print_f, stdout)
        elif variante == 'ptpt':
            completo(paragrafos, 569, caminho+'ptpt.train', print_f, stdout)
        elif variante == 'mix':
            completo_mix(paragrafos, 569, caminho+'harem.train', caminho+'harem.test', print_f, stdout)
    else:
        ajuda()

def ajuda():
        print('Instruções de uso: opennlp.py [arquivo-harem] [opcao] [variante] [porcentagem]')
        print('opcao:')
        print('\tholdout')
        print('\tcompleto')
        print('variante:')
        print('\tptbr')
        print('\tptpt')
        print('\tmix')
        print('porcentagem:')
        print('\t0.0 - 1.0')
