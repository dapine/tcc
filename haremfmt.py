import argparse
import bs4
import sys

import opennlp
import corenlp
import iob

from harem import *

stdout = sys.stdout

parser = argparse.ArgumentParser(description='HAREM Formatter')

parser.add_argument('filename', metavar='filename', type=str, nargs=1,
        help='XML HAREM file')
parser.add_argument('-o', '--output',
        help='Output format. Either opennlp, corenlp, spacy')
parser.add_argument('-s', '--split', type=float,
        help='Splits output given percentage')
parser.add_argument('-l', '--level', type=str,
        help='Split level. Either "entity", "paragraph", "document"')
parser.add_argument('-v', '--variant', type=str,
        help='Portuguese variant. Either "pt-br" or "pt-pt"')

args = parser.parse_args()
vargs = vars(args)

filename = vargs['filename'][0]
output = vargs['output']
split = vargs['split']
level = vargs['level']
variant = vargs['variant'] or 'harem'

f = open(filename, 'r')
metadata = open('/home/d/tcc/harem/colSegundoHAREM-meta.xml', 'r')

documents = get_docs(f)
paragraphs = get_paragraphs(documents)

# List comprehend this
ptbr_docs = []
ptpt_docs = []
for doc in documents:
    if doc.variant == 'pt_BR':
        ptbr_docs.append(doc)
    elif doc.variant == 'pt_PT':
        ptpt_docs.append(doc)

MAX_DOCS_PTBR = len(ptbr_docs)
MAX_DOCS_PTPT = len(ptpt_docs)
MAX_DOCS_MIX = len(documents)
MAX_PARA_PTBR = len(get_paragraphs(ptbr_docs))
MAX_PARA_PTPT = len(get_paragraphs(ptpt_docs))
MAX_PARA_MIX = len(paragraphs)

# levels = {
#         'document': documents,
#         'paragraph': paragraphs
# }

printers = {
        'opennlp': { 'document': opennlp.print_docs,
                     'paragraph': opennlp.print_ps },
        'corenlp': { 'document': corenlp.print_docs,
                     'paragraph': corenlp.print_ps },
        'spacy':   { 'document': iob.print_docs,
                     'paragraph': iob.print_ps },
}

variants = {
        'pt-br': { 'document': ptbr_docs[0:MAX_DOCS_PTBR], 'paragraph': get_paragraphs(ptbr_docs)[0:MAX_PARA_PTBR] },
        'pt-pt': { 'document': ptpt_docs[0:MAX_DOCS_PTBR], 'paragraph': get_paragraphs(ptpt_docs)[0:MAX_PARA_PTBR] },
        'mix': { 'document': documents[0:MAX_DOCS_PTBR], 'paragraph': paragraphs[0:MAX_PARA_PTBR] },
        'harem': { 'document': documents, 'paragraph': paragraphs },
}

kfold(variants[variant][level], 10, output, printers[output][level], stdout)

# train_test(variants[variant][level], round(len(variants[variant][level])*split),
#         variant+'.train', variant+'.test', printers[output][level], stdout)
