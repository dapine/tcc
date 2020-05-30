import nltk
from nltk.corpus import floresta
from nltk import word_tokenize

def simplify_tag(t):
    if "+" in t:
        return t[t.index("+")+1:]
    else:
        return t

texto = "François-Marie Arouet, mais conhecido pelo pseudônimo Voltaire (Paris, 21 de novembro de 1694 — Paris, 30 de maio de 1778), foi um escritor, ensaísta, deísta e filósofo iluminista francês."

toks = word_tokenize(texto)
tsents = floresta.tagged_sents()
tsents = [[(w.lower(),simplify_tag(t)) for (w,t) in sent] for sent in tsents if sent]

# tsents total = 9266
# 70%
train = tsents[6487:]
# 30%
test = tsents[:2779]

tagger0 = nltk.DefaultTagger('n')
tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
tagger2 = nltk.BigramTagger(train, backoff=tagger1)

print(tagger2.tag(toks))
print(tagger2.evaluate(test))
