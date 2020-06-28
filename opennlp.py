import bs4
from harem import *
import sys

stdout = sys.stdout

filename = sys.argv[1]
opcao = sys.argv[2]
variante = sys.argv[3]
porcentagem = sys.argv[4]

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

def media(paragrafos, func):
    x = list(filter(lambda x : x != 0, func(paragrafos)))

    return sum(x) / len(x)

def print_ps(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None and '|' in t.categoria:
                    cat = t.categoria.split('|')[0]

                print(' <START:{}> {} <END> '.format(cat, t.texto), end='')
            else:
                print(t.texto, end='')

documentos = get_docs(f)
paragrafos = todos_paragrafos(documentos)

# print(media(paragrafos, entidades_por_paragrafo))

# cli(paragrafos, opcao, variante, 'tmp/opennlp/', print_ps, stdout, porcentagem)
