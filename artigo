# PANDA: Plataforma de Análise Neural Digital Amigável

## Introdução

A inteligência artificial (IA) está cada vez mais presente em nossas vidas, facilitando processos e proporcionando novas formas de interagir com a tecnologia. Hoje, vamos apresentar o PANDA, uma IA desenvolvida em Python que consegue identificar a emoção contida em um texto, classificando-a como positiva, negativa ou neutra. O PANDA é simples e utiliza um banco de palavras para realizar essa análise, tornando-o acessível e eficiente.

Neste artigo, vamos explorar detalhadamente o código do PANDA, explicando cada bloco para que você possa entender como ele funciona e até mesmo aplicar sozinho. Então, vamos começar!

## O Código do PANDA

### Importações e Preparações


import re
```

Aqui, estamos importando o módulo `re` (expressões regulares) que nos ajudará a dividir o comentário em palavras individuais.

### Função `carrega_lexico`


def carrega_lexico():
    sentilexpt = open('SentiLex-lem-PT02.txt','r')
    dic_palavra_polaridade = {}
    for i in sentilexpt.readlines():
        pos_ponto = i.find('.')
        palavra = (i[:pos_ponto])
        pol_pos = i.find('POL')
        polaridade = (i[pol_pos+7:pol_pos+9]).replace(';','')
        dic_palavra_polaridade[palavra] = polaridade
    return dic_palavra_polaridade
```

Esta função abre um arquivo chamado `SentiLex-lem-PT02.txt`, que contém palavras e suas respectivas polaridades (positivas, negativas ou neutras). A função lê cada linha do arquivo, extrai a palavra e sua polaridade, e armazena essa informação em um dicionário (`dic_palavra_polaridade`). Esse dicionário é retornado pela função para ser usado posteriormente.

### Função `analyze_sentiment`


def analyze_sentiment():
    comentario = input("Como você está se sentindo hoje? ")
```

Esta parte do código solicita ao usuário que insira um comentário, perguntando como ele está se sentindo.


    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
```

Aqui, usamos a expressão regular para dividir o comentário em palavras individuais, garantindo que todas estejam em letras minúsculas para facilitar a comparação.


    sentilex = carrega_lexico()
```

Chamamos a função `carrega_lexico` para obter o dicionário de palavras e suas polaridades.

```python
    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(sentilex.get(palavra, 0) == '1' for palavra in palavras)
    count_negativo = sum(sentilex.get(palavra, 0) == '-1' for palavra in palavras)
    count_neutro = sum(sentilex.get(palavra, 0) == '0' for palavra in palavras)
```

Contamos quantas palavras positivas, negativas e neutras estão presentes no comentário. Usamos a função `sum` junto com expressões geradoras para contar as ocorrências de cada tipo de palavra.


    # Verifica se há mais palavras positivas do que negativas e neutras no comentário. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo:
        return "Positivo"
    elif count_negativo > count_positivo:
        return "Negativo"
    else:
        return "Neutro"
```

Finalmente, comparamos as contagens de palavras positivas e negativas para determinar o sentimento geral do comentário. Se houver mais palavras positivas do que negativas, o sentimento é classificado como "Positivo". Se houver mais palavras negativas, o sentimento é "Negativo". Caso contrário, é "Neutro".

### Executando a Análise


# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
```

Chamamos a função `analyze_sentiment` e imprimimos o resultado, que será o sentimento identificado: positivo, negativo ou neutro.

## Conclusão

O PANDA é uma IA simples, mas poderosa, que pode ser facilmente compreendida e implementada por qualquer pessoa interessada em análise de sentimentos. Usando Python e um banco de palavras, ele consegue identificar a emoção em um texto de maneira eficiente. Esperamos que este artigo tenha ajudado você a entender melhor como o PANDA funciona e que você se sinta inspirado a explorar mais o mundo da inteligência artificial.

Experimente o código, faça suas próprias modificações e veja como é divertido trabalhar com IA!
