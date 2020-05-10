# from xml.dom.minidom import parse

# xml = parse('harem.xml')

# docs = xml.getElementsByTagName('DOC')

# for doc in docs:
#     print('-DOCSTART- -X- O O\n')
#     cn = doc.childNodes
#     for n in cn:
#         if n.nodeType != n.TEXT_NODE:
#             p = n.childNodes
#             for em in p:
#                 if em.nodeType != em.TEXT_NODE:
#                     cat = em.getAttribute('CATEG')
#                     valor = em.firstChild.nodeValue
#                     if cat == None or valor == None or cat.isspace() or valor.isspace() or cat == '' or valor == '':
#                         pass
#                     else:
#                         if '|' in cat:
#                             newcat = cat.split('|')[0]

#                             if ' ' in valor:
#                                 valor = valor.split(' ')
#                                 for i, v in enumerate(valor):
#                                     if i == 0:
#                                         print('{0} -X- O B-{1}'.format(v.strip(), newcat))
#                                     else:
#                                         print('{0} -X- O I-{1}'.format(v.strip(), newcat))
#                             else:
#                                 print('{0} -X- O I-{1}'.format(valor.strip(), newcat))
#                         else:
#                             if ' ' in valor:
#                                 valor = valor.split(' ')
#                                 for i, v in enumerate(valor):
#                                     if i == 0:
#                                         print('{0} -X- O B-{1}'.format(v.strip(), cat))
#                                     else:
#                                         print('{0} -X- O I-{1}'.format(v.strip(), cat))
#                             else:
#                                 print('{0} -X- O I-{1}'.format(valor.strip(), cat))
#                 else:
#                     toks = em.nodeValue.split()
#                     for tok in toks:
#                         if tok != '':
#                             print('{0} -X- O {1}'.format(tok, 'O'))
#         else:
#             pass


import bs4
import nltk
from bs4 import BeautifulSoup

f = open('harem-utf8.xml', 'r')

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

for doc in docs:
    for p in doc.contents:
        pp(p)
        print()
