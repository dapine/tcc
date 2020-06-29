import bs4
from harem import *
import sys

stdout = sys.stdout

filename = sys.argv[1]

f = open(filename, 'r')

def palavras_por_paragrafo(paragrafos):
    c = []
    for p in paragrafos:
        ps = 0
        for t in p.lista:
            if t.t == 'em':
                ps += 1
            else:
                ps += 1
        c.append(ps)
    return c

def entidades_por_paragrafo(paragrafos):
    c = []
    for p in paragrafos:
        ps = 0
        for t in p.lista:
            if t.t == 'em':
                ps += 1
        c.append(ps)
    return c

def palavras_por_documento(documentos):
    x = []
    for doc in documentos:
        c = 0
        for p in doc.paragrafos:
            for t in p.lista:
                c += 1
        x.append(c)
    return x

def entidades_por_documento(documentos):
    x = []
    for doc in documentos:
        c = 0
        for p in doc.paragrafos:
            for t in p.lista:
                if t.t == 'em':
                    c += 1
        x.append(c)
    return x

def media(paragrafos, func):
    x = list(filter(lambda x : x != 0, func(paragrafos)))

    return sum(x) / len(x)

documentos = get_docs(f)
paragrafos = todos_paragrafos(documentos)


# print(media(documentos, palavras_por_documento))
print(media(documentos, entidades_por_documento))

# print(media(paragrafos, entidades_por_paragrafo))
