# tcc

## OpenNLP

### Treinamento

```
$ opennlp TokenNameFinderTrainer -model <saída(modelo treinado)> -lang <língua> -data <corpus> -encoding <codificação dos caracteres>
```

Ex.:

```
$ opennlp TokenNameFinderTrainer -model modelo-harem-opennlp.bin -lang pt -data tmp/harem-opennlp.txt -encoding UTF-8
```

### Execução

```
$ opennlp TokenNameFinder <modelo>
```

Neste caso, os dados são lidos stdin, então podemos redirecionar um arquivo de texto como entrada:

```
$ opennlp TokenNameFinder <modelo> < <entrada>
```

Links úteis:

[Documentação OpenNLP](https://opennlp.apache.org/docs/1.5.3/manual/opennlp.html#tools.namefind)

## CoreNLP

### Treinamento

Primeiro é necessário criar o aquivo de propriedades no treinamento do modelo.
Um exemplo é:

```
# location of the training file
trainFile = jane-austen-emma-ch1.tsv
# location where you would like to save (serialize) your
# classifier; adding .gz at the end automatically gzips the file,
# making it smaller, and faster to load
serializeTo = ner-model.ser.gz

# structure of your training file; this tells the classifier that
# the word is in column 0 and the correct answer is in column 1
map = word=0,answer=1

# This specifies the order of the CRF: order 1 means that features
# apply at most to a class pair of previous class and current class
# or current class and next class.
maxLeft=1

# these are the features we'd like to train with
# some are discussed below, the rest can be
# understood by looking at NERFeatureFactory
useClassFeature=true
useWord=true
# word character ngrams will be included up to length 6 as prefixes
# and suffixes only
useNGrams=true
noMidNGrams=true
maxNGramLeng=6
usePrev=true
useNext=true
useDisjunctive=true
useSequences=true
usePrevSequences=true
# the last 4 properties deal with word shape features
useTypeSeqs=true
useTypeSeqs2=true
useTypeySequences=true
wordShape=chris2useLC
```

Após isso, devemos executar o arquivo to-corenlp.py para transformar o corpus HAREM para o formato padrão do CoreNLP.

Então, após possuirmos esses dois arquivos preparados, executamos o comando para realização do treinamento:

```
$ java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop <arquivo de propriedade>
```

Ao término do treinamento, um arquivo com o modelo treinado é gerado. Ele vai ter o mesmo nome de arquivo definido nas propriedades.

### Execução

O arquivo de entrada precisa estar no formato definido. Então, caso esteja em formato natural, se deve executar os seguintes comandos:

```
$ java -cp stanford-ner.jar edu.stanford.nlp.process.PTBTokenizer jane-austen-emma-ch1.txt > jane-austen-emma-ch1.tok
```

Para tokenizar o texto e deixar cada token em uma linha.

Após isso, executamos este comando em perl para inserir categorias ao lado do token, separando por uma tabulação:

```
$ perl -ne 'chomp; print "$_\tO\n"' jane-austen-emma-ch1.tok > jane-austen-emma-ch1.tsv
```

Feito isso, temos o arquivo no formato exigido pelo CoreNLP e para anotarmos utilizando o nosso modelo criado, executamos:

```
$ java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -testFile jane-austen-emma-ch2.tsv
```

Links úteis:

[FAQ Stanford NER CRF](https://nlp.stanford.edu/software/crf-faq.html#a)

## spaCy

Primeiro é necessário converter o corpus original (arquivo .xml) no formato aceito pela ferramenta de linha de comando do spaCy. Esses formatos são: conll, conllu, conllubio, ner (etiquetas IOB/IOB2 com um token por linha), iob e jsonl.

O arquivo to-iob.py converte o HAREM em XML para o formato iob. Então, precisamos primeiro executar o comando:

```
$ python3 to-iob.py > harem.iob
```

para gerar o arquivo neste formato. Após isso, executamos a ferramenta do spaCy para converter nosso formato IOB para JSON.

```
$ python -m spacy convert [input_file] [output_dir] [--file-type] [--converter]
[--n-sents] [--morphology] [--lang]
```
```
$ python3 -m spacy convert harem.iob . -c iob
```

Então, nosso corpus de treinamento está em formato `.json` aceito pela ferramenta.
O próximo passo é treinar o modelo. Para isso, o comando é:

```
$ python -m spacy train [lang] [output_path] [train_path] [dev_path]
[--base-model] [--pipeline] [--vectors] [--n-iter] [--n-early-stopping]
[--n-examples] [--use-gpu] [--version] [--meta-path] [--init-tok2vec]
[--parser-multitasks] [--entity-multitasks] [--gold-preproc] [--noise-level]
[--orth-variant-level] [--learn-tokens] [--textcat-arch] [--textcat-multilabel]
[--textcat-positive-label] [--verbose]
```

Ex.:

```
$ python3 -m spacy train pt models harem.json harem-dev.json
```

Após isso, a pasta `models` é criada, com todos os modelo para cada iteração junto com o melhor modelo (model-best) e o modelo final (model-final).

Agora, basta carregar este modelo para que se possa identificar as entidades. Isso pode ser feito através do próprio REPL do Python.

```
$ python3

>>> import spacy
>>> nlp = spacy.load('models/model-best')
>>> doc = nlp('A língua portuguesa, também designada português, é uma língua românica flexiva ocidental originada no galego-português falado no Reino da Galiza e no norte de Portugal.')
>>> for ent in doc.ents:
...     print(ent.text, ent.label_)
...
Reino LOC
Galiza ORG
Portugal LOC
```

Links úteis:

[CLI spaCy](https://spacy.io/api/cli)
[Carregando e usando modelos](https://spacy.io/usage/saving-loading#models)
