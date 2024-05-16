import re
import nltk 
from nltk.corpus import opinion_lexicon
nltk.download('opinion_lexicon')

def analyze_sentiment():
    comentario = input()

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())

    positivas = set(opinion_lexicon.positive())
    negativas = set(opinion_lexicon.negative())

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)

    # Verifica se há negação na frase
    for i, palavra in enumerate(palavras[:-1]):
        if palavra == "não" and (palavras[i+1] in positivas or palavras[i+1] in negativas):
            if palavras[i+1] in positivas:
                count_positivo -= 1
                count_negativo += 1
            else:
                count_negativo -= 1
                count_positivo += 1

    # Verifica se há mais palavras positivas do que negativas.
    if count_positivo > count_negativo:
        return "Positivo"
    elif count_negativo > count_positivo:
        return "Negativo"
    else:
        return "Indeterminado"
    

# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
