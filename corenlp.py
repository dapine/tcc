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

def print_ps_sem_acento(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None and '|' in t.categoria:
                    cat = t.categoria.split('|')[0]

                tokens = t.texto.split()

                for tok in tokens:
                    print('{}\t{}'.format(remover_acentuacao(tok), cat))
            else:
                tokens = t.texto.split()

                for tok in tokens:
                    print('{}\t{}'.format(remover_acentuacao(tok), 'O'))

def print_docs(documentos):
    for doc in documentos:
        for p in doc.paragrafos:
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

def print_docs_sem_acento(documentos):
    for doc in documentos:
        for p in doc.paragrafos:
            for t in p.lista:
                if t.t == 'em':
                    cat = t.categoria
                    if t.categoria != None and '|' in t.categoria:
                        cat = t.categoria.split('|')[0]

                    tokens = t.texto.split()

                    for tok in tokens:
                        print('{}\t{}'.format(remover_acentuacao(tok), cat))
                else:
                    tokens = t.texto.split()

                    for tok in tokens:
                        print('{}\t{}'.format(remover_acentuacao(tok), 'O'))
