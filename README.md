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
