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

def print_ps_sem_acento(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None and '|' in t.categoria:
                    cat = t.categoria.split('|')[0]

                print(' <START:{}> {} <END> '.format(cat, remover_acentuacao(t.texto)), end='')
            else:
                print(remover_acentuacao(t.texto), end='')

def print_docs(documentos):
    for doc in documentos:
        for p in doc.paragrafos:
            for t in p.lista:
                if t.t == 'em':
                    cat = t.categoria
                    if t.categoria != None and '|' in t.categoria:
                        cat = t.categoria.split('|')[0]

                    print(' <START:{}> {} <END> '.format(cat, t.texto), end='')
                else:
                    print(t.texto, end='')

def print_docs_sem_acento(documentos):
    for doc in documentos:
        for p in doc.paragrafos:
            for t in p.lista:
                if t.t == 'em':
                    cat = t.categoria
                    if t.categoria != None and '|' in t.categoria:
                        cat = t.categoria.split('|')[0]

                    print(' <START:{}> {} <END> '.format(cat, t.texto), end='')
                else:
                    print(t.texto, end='')
