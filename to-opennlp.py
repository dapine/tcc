import bs4
import nltk
import sys
from bs4 import BeautifulSoup
from unicodedata import normalize

filename = sys.argv[1]

f = open(filename, 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

def remover_pontuacao(string):
    tokens = nltk.word_tokenize(string)

    words = [t for t in tokens if t.isalnum()]

    return ' '.join(words)

def remover_acentuacao(string):
    return normalize('NFKD', string).encode('ascii', 'ignore').decode('ascii')

def pp(p, pontuacao=True):
    if type(p) is bs4.element.Tag:
        if p.name == 'em':
            texto = p.string
            categ = p.get('categ')
            if categ is None:
                print(remover_acentuacao(texto), end='')
            else:
                if '|' in categ:
                    categ = categ.split('|')[0]

                print(' <START:{0}> {1} <END> '.format(categ, remover_acentuacao(texto)), end='')
        else:
            for x in p.contents:
                pp(x)
    else:
        if pontuacao:
            tokens = nltk.word_tokenize(p.string)
            print(remover_acentuacao(' '.join(tokens)), end='')
        else:
            print(remover_pontuacao(p.string), end='')

sents = []

for doc in docs:
    for p in doc.contents:
        sents.append(p)
    # sents.append("-enddoc-")

sent_min = 0
sent_max = 1973

limite_sent = sents[sent_min:sent_max]

for p in limite_sent:
    pp(p)
    print()

print(len(sents))
