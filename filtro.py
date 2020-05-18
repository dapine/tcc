import bs4
import nltk
import sys
from bs4 import BeautifulSoup

corpus = sys.argv[1]
metadata = sys.argv[2]

fc = open(corpus, 'r')
fm = open(metadata, 'r')

soup_c = BeautifulSoup(fc, 'lxml')
soup_m = BeautifulSoup(fm, 'lxml')

docs_corpus = soup_c.find_all('doc')

def variante(doc, soup_meta):
    v = soup_meta.find_all(attrs={"docid": doc.get('docid')})

    return v[0].find("variante").get_text()

def pt_pt(docs, soup_meta):
    d = []

    for doc in docs:
        if variante(doc, soup_meta) == 'pt_PT':
            d.append(doc)

    return d

def pt_br(docs, soup_meta):
    d = []

    for doc in docs:
        if variante(doc, soup_meta) == 'pt_BR':
            d.append(doc)

    return d

def pretty(docs):
    s = ''
    for doc in docs:
        s += doc.prettify()

    return s

print(pretty(pt_pt(docs_corpus, soup_m)))
# print(pretty(pt_br(docs_corpus, soup_m)))
