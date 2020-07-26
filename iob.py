def print_ps(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None:
                    if '|' in t.categoria:
                        cat = t.categoria.split('|')[0]

                    tokens = t.texto.split()

                    for i, tok in enumerate(tokens):
                        if i == 0:
                            print('{0} -X- O B-{1}'.format(tok, cat))
                        else:
                            print('{0} -X- O I-{1}'.format(tok, cat))
            else:
                tokens = t.texto.split()

                for tok in tokens:
                    print('{0} -X- O {1}'.format(tok, 'O'))

def print_docs(documentos):
    for doc in documentos:
        for p in doc.paragrafos:
            for t in p.lista:
                if t.t == 'em':
                    cat = t.categoria
                    if t.categoria != None:
                        if '|' in t.categoria:
                            cat = t.categoria.split('|')[0]

                        tokens = t.texto.split()

                        for i, tok in enumerate(tokens):
                            if i == 0:
                                print('{0} -X- O B-{1}'.format(tok, cat))
                            else:
                                print('{0} -X- O I-{1}'.format(tok, cat))
                else:
                    tokens = t.texto.split()

                    for tok in tokens:
                        print('{0} -X- O {1}'.format(tok, 'O'))
        print()

def print_ps_sem_acento(paragrafos):
    for p in paragrafos:
        for t in p.lista:
            if t.t == 'em':
                cat = t.categoria
                if t.categoria != None:
                    if '|' in t.categoria:
                        cat = t.categoria.split('|')[0]

                    tokens = t.texto.split()

                    for i, tok in enumerate(tokens):
                        if i == 0:
                            print('{0} -X- O B-{1}'.format(remover_acentuacao(tok), cat))
                        else:
                            print('{0} -X- O I-{1}'.format(remover_acentuacao(tok), cat))
            else:
                tokens = t.texto.split()

                for tok in tokens:
                    print('{0} -X- O {1}'.format(remover_acentuacao(tok), 'O'))

def print_docs_sem_acento(paragrafos):
    for doc in docs:
        for p in docs.paragrafos:
            for t in p.lista:
                if t.t == 'em':
                    cat = t.categoria
                    if t.categoria != None:
                        if '|' in t.categoria:
                            cat = t.categoria.split('|')[0]

                        tokens = t.texto.split()

                        for i, tok in enumerate(tokens):
                            if i == 0:
                                print('{0} -X- O B-{1}'.format(remover_acentuacao(tok), cat))
                            else:
                                print('{0} -X- O I-{1}'.format(remover_acentuacao(tok), cat))
                else:
                    tokens = t.texto.split()

                    for tok in tokens:
                        print('{0} -X- O {1}'.format(remover_acentuacao(tok), 'O'))
