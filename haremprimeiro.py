import bs4

class Doc:
    def __init__(self, tag):
        if type(tag) is bs4.element.Tag and tag.name == 'doc':
            self.lista = []
            self.id = tag.get('id')

            for e in tag.contents:
                self.lista.append(Em(e))

class Em:
    def __init__(self, tag):
        if type(tag.string) != type(None):
            if type(tag) is bs4.element.Tag:
                if tag.name == 'alt':
                    pass
                else:
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
