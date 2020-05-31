import bs4
import nltk
import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

f = open(filename, 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

def remover_pontuacao(string):
    tokens = nltk.word_tokenize(string)

    words = [t for t in tokens if t.isalnum()]

    return ' '.join(words)

def pp(p, pontuacao=True):
    if type(p) is bs4.element.Tag:
        if p.name == 'em':
            texto = p.string
            categ = p.get('categ')
            if categ is None:
                print(texto, end='')
            else:
                if '|' in categ:
                    categ = categ.split('|')[0]

                print(' <START:{0}> {1} <END> '.format(categ, texto), end='')
        else:
            for x in p.contents:
                pp(x)
    else:
        if pontuacao:
            tokens = nltk.word_tokenize(p.string)
            print(' '.join(tokens), end='')
        else:
            print(remover_pontuacao(p.string), end='')

sents = []

for doc in docs:
    for p in doc.contents:
        sents.append(p)

sent_min = 4177
sent_max = 4677

limite_sent = sents[sent_min:sent_max]

for p in limite_sent:
    pp(p)
    print()
