from xml.dom.minidom import parse

xml = parse('harem.xml')

docs = xml.getElementsByTagName('DOC')

for doc in docs:
    print('-DOCSTART- -X- O O\n')
    cn = doc.childNodes
    for n in cn:
        if n.nodeType != n.TEXT_NODE:
            p = n.childNodes
            for em in p:
                if em.nodeType != em.TEXT_NODE:
                    cat = em.getAttribute('CATEG')
                    valor = em.firstChild.nodeValue
                    if cat == None or valor == None or cat.isspace() or valor.isspace() or cat == '' or valor == '':
                        pass
                    else:
                        if '|' in cat:
                            newcat = cat.split('|')[0]

                            if ' ' in valor:
                                valor = valor.split(' ')
                                for v in valor:
                                    print('{0} -X- O {1}'.format(v.strip(), newcat))
                            else:
                                print('{0} -X- O {1}'.format(valor.strip(), newcat))
                        else:
                            if ' ' in valor:
                                valor = valor.split(' ')
                                for v in valor:
                                    print('{0} -X- O {1}'.format(v.strip(), cat))
                            else:
                                print('{0} -X- O {1}'.format(valor.strip(), cat))
                else:
                    toks = em.nodeValue.split()
                    for tok in toks:
                        if tok != '':
                            print('{0} -X- O {1}'.format(tok, 'O'))
        else:
            pass
