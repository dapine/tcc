import bs4
import nltk
import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

f = open(filename, 'r')

soup = BeautifulSoup(f, 'lxml')

docs = soup.find_all('doc')

def pp(p):
    if type(p) is bs4.element.Tag:
        if p.name == 'em':
            categ = p.get('categ')
            valor = p.string
            if categ is None:
                print(valor, end='')
            else:
                if '|' in categ:
                    categ = categ.split('|')[0]

                if ' ' in valor:
                    valor = valor.split()

                    for i, v in enumerate(valor):
                        if i == 0:
                            print('{0} -X- O B-{1}'.format(v, categ))
                        else:
                            print('{0} -X- O I-{1}'.format(v, categ))
                else:
                    print('{0} -X- O I-{1}'.format(valor, categ))
        else:
            for x in p.contents:
                pp(x)
    else:
        tokens = nltk.word_tokenize(p.string)
        for tok in tokens:
            print('{0} -X- O {1}'.format(tok, 'O'))

sents = []

for doc in docs:
    for p in doc.contents:
        sents.append(p)

sent_min = 0
sent_max = 1324

limite_sent = sents[sent_min:sent_max]

for p in limite_sent:
    pp(p)
    print()
