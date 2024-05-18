import re
#import nltk 
#from nltk.corpus import opinion_lexicon
#nltk.download('opinion_lexicon')

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

def analyze_sentiment():
    comentario = input("Como você está se sentindo hoje? ")

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())

    sentilex = carrega_lexico()

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(sentilex.get(palavra, 0) == '1' for palavra in palavras)
    count_negativo = sum(sentilex.get(palavra, 0) == '-1' for palavra in palavras)
    count_neutro = sum(sentilex.get(palavra, 0) == '0' for palavra in palavras)

    # Verifica se há mais palavras positivas do que negativas e neutras no comentário. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo:
        return "Positivo"
    elif count_negativo > count_positivo:
        return "Negativo"
    else:
        return "Neutro" 
    

# Saída esperada
sentimento = analyze_sentiment()
print("Sentimento:", sentimento)
