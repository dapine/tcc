import bs4

class Doc:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag and tag.name == 'doc':
            self.paragrafos = []
            self.id = tag.get('id')
            for p in tag.contents:
                self.paragrafos.append(P(p))

class P:
    def __init__(self, tag):
        self.lista = []
        if type(tag) is bs4.element.Tag and tag.name == 'p':
            for e in tag.contents:
                self.lista.append(Em(e))

class Em:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag:
            self.categoria = tag.get('categ')
            self.texto = tag.string.strip()
            self.id = tag.get('id')
            self.tipo = tag.get('tipo')
            self.t = 'em'
        else:
            self.categoria = ''
            self.texto = tag.string.strip()
            self.id = ''
            self.tipo = ''
            self.t = 'plain_text'
