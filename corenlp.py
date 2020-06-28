import bs4
import sys
from harem import *

stdout = sys.stdout

filename = sys.argv[1]
opcao = sys.argv[2]
variante = sys.argv[3]
porcentagem = sys.argv[4]

f = open(filename, 'r')

def print_ps(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None and '|' in t.categoria:
                    cat = t.categoria.split('|')[0]

                tokens = t.texto.split()

                for tok in tokens:
                    print('{}\t{}'.format(tok, cat))
            else:
                tokens = t.texto.split()

                for tok in tokens:
                    print('{}\t{}'.format(tok, 'O'))


documentos = get_docs(f)
paragrafos = todos_paragrafos(documentos)

cli(paragrafos, opcao, variante, 'tmp/corenlp/', print_ps, stdout, porcentagem)
