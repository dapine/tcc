import bs4
from bs4 import BeautifulSoup
import random
import sys
import unicodedata

metadata = open('/home/d/tcc/harem/metadata-segundo-harem-utf8.xml', 'r')
soup_meta = BeautifulSoup(metadata, 'lxml')

class Doc:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag and tag.name == 'doc':
            self.paragrafos = []
            self.id = tag.get('id')
            self.variant = variant(tag, soup_meta)
            for p in tag.contents:
                self.paragrafos.append(P(p))

class P:
    def __init__(self, tag):
        self.lista = []
        if type(tag) is bs4.element.Tag and tag.name == 'p':
            for e in tag.contents:
                if e.name == 'alt':
                    self.lista = self.lista + choose_alt(e, 1)
                elif e.name == 'omitido':
                    pass
                else:
                    self.lista.append(Em(e))

class Em:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag and tag.name == 'em':
            self.categoria = tag.get('categ')
            self.texto = tag.string.strip()
            self.id = tag.get('id')
            self.tipo = tag.get('tipo')
            self.t = 'em'
        else:
            if tag.string != None:
                self.categoria = ''
                self.texto = tag.string.strip()
                self.id = ''
                self.tipo = ''
                self.t = 'plain_text'

def choose_alt(tag, order=0):
    ems = []

    if order == 0:
        for em in tag.contents:
            if len(em) >= 3:
                if em == ' | ' or em[0:3] == ' | ':
                    break

            ems.append(Em(em))

    elif order == 1:
        ic = 0
        for em in tag.contents:
            if len(em) >= 3:
                if em == ' | ':
                    ic += 1
                    break
                elif em[0:3] == ' | ':
                    break

            ic += 1

        for em in tag.contents[ic:len(tag.contents)]:
            ems.append(Em(em))

    return ems

def get_docs(f):
    soup = BeautifulSoup(f, 'lxml')
    docs = soup.find_all('doc')

    documentos = []

    for doc in docs:
        documentos.append(Doc(doc))

    return documentos

def get_paragraphs(docs):
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

def train_test(paragrafos, n, out_treino, out_teste, print_f, stdout):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]
    teste = paragrafos[n+1:len(paragrafos)]

    print_file(treino, out_treino, print_f, stdout)
    print_file(teste, out_teste, print_f, stdout)

def completo_mix(paragrafos, n, out_treino, out_teste, print_f, stdout):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]
    teste = paragrafos[n+1:(n+n+1)]

    print_file(treino, out_treino, print_f, stdout)
    print_file(teste, out_teste, print_f, stdout)

def completo(paragrafos, n, saida, print_f, stdout):
    random.shuffle(paragrafos)

    treino = paragrafos[0:n]

    print_file(treino, saida, print_f, stdout)

def remover_acentuacao(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def variant(doc, soup_meta):
    v = soup_meta.find_all(attrs={"docid": doc.get('docid')})

    return v[0].find("variante").get_text()
