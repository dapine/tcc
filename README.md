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
