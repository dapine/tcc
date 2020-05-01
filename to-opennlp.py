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
                        print(' <START:{0}> {1} <END> '.format(cat, valor.strip()), end = '')
                else:
                    print(em.nodeValue, end = '')
        else:
            print(n.nodeValue, end = '')
