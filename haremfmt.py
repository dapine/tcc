import argparse
import bs4
import sys

import opennlp
import corenlp

from harem import *

stdout = sys.stdout

parser = argparse.ArgumentParser(description='HAREM Formatter')
parser.add_argument('filename', metavar='filename', type=str, nargs=1, help='XML HAREM file')
parser.add_argument('-o', '--output', help='Output format. Either opennlp, corenlp, spacy')
parser.add_argument('-s', '--split', type=float, help='Splits output given percentage')
parser.add_argument('-l', '--level', type=str, help='Split level. Either "entity", "paragraph", "document"')
parser.add_argument('-v', '--variant', type=str, help='Portuguese variant. Either "pt-br" or "pt-pt"')

args = parser.parse_args()
vargs = vars(args)

filename = vargs['filename'][0]
output = vargs['output']
split = vargs['split']
level = vargs['level']
variant = vargs['variant']
if variant is None:
    variant = 'harem'

f = open(filename, 'r')

documentos = get_docs(f)
paragrafos = todos_paragrafos(documentos)

levels = {
        'document': documentos,
        'paragraph': paragrafos
}

printers = {
        'opennlp': { 'document': opennlp.print_docs,
                     'paragraph': opennlp.print_ps },
        'corenlp': { 'document': corenlp.print_docs,
                     'paragraph': corenlp.print_ps },
}

treino_teste(levels[level], round(len(levels[level])*split), variant+'.train', variant+'.test', printers[output][level], stdout)
