from xml.dom.minidom import parse

xml = parse('harem.xml')

docs = xml.getElementsByTagName('DOC')

for doc in docs:
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
                            print('{0}\t{1}'.format(valor.strip(), newcat))
                        else:
                            print('{0}\t{1}'.format(valor.strip(), cat))
                else:
                    toks = em.nodeValue.split()
                    for tok in toks:
                        if tok != '':
                            print('{0}\t{1}'.format(tok, 'O'))
                    # print(em.nodeValue)
        else:
            pass
            # print(n)
            # print(n.nodeValue)
