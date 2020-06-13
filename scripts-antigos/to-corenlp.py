import bs4
import nltk
import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

f = open(filename, 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

def pp(p, pontuacao=True):
    if type(p) is bs4.element.Tag:
        if p.name == 'em':
            categ = p.get('categ')
            if categ is None:
                print(p.string, end='')
            else:
                if '|' in categ:
                    categ = categ.split('|')[0]

                print('{0}\t{1}'.format(p.string, categ))
        else:
            for x in p.contents:
                pp(x, pontuacao)
    else:
        tokens = nltk.word_tokenize(p.string)
        for tok in tokens:
            if pontuacao:
                print('{0}\t{1}'.format(tok, 'O'))
            else:
                if tok.isalnum():
                    print('{0}\t{1}'.format(tok, 'O'))

sents = []

for doc in docs:
    for p in doc.contents:
        sents.append(p)

sent_min = 1974
sent_max = 2773

limite_sent = sents[sent_min:sent_max]

for p in limite_sent:
    pp(p)
    print()
