import re
#import nltk 
#from nltk.corpus import opinion_lexicon
#nltk.download('opinion_lexicon')

def carrega_lexico(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_lexico:
            dic_palavra_polaridade = {}
            for linha in arquivo_lexico:
                pos_ponto = linha.find('.')
                palavra = linha[:pos_ponto]
                pol_pos = linha.find('POL')
                polaridade = linha[pol_pos + 7:pol_pos + 9].replace(';', '')
                dic_palavra_polaridade[palavra] = polaridade
        return dic_palavra_polaridade
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return {}
    except Exception as e:
        print(f"Erro ao carregar o léxico: {e}")
        return {}

def analyze_sentiment(sentilex):
    comentario = input("Como você está se sentindo hoje? ")

    # Divisão do comentário em palavras usando uma expressão regular melhorada
    palavras = re.findall(r'\b\w+(?:[-\']\w+)*\b', comentario.lower())

    if not sentilex:
        return "Não foi possível realizar a análise de sentimento."

    # Contagem de palavras positivas, negativas e neutras
    count_positivo, count_negativo, count_neutro = 0, 0, 0
    for palavra in palavras:
        polaridade = sentilex.get(palavra, '0')
        if polaridade == '1':
            count_positivo += 1
        elif polaridade == '-1':
            count_negativo += 1
        else:
            count_neutro += 1

    # Verifica se há mais palavras positivas do que negativas e neutras no comentário.
    if count_positivo > count_negativo:
        return "Positivo"
    elif count_negativo > count_positivo:
        return "Negativo"
    else:
        return "Neutro" 

def main():
    try:
        # Caminho do arquivo léxico
        caminho_arquivo_lexico = 'SentiLex-lem-PT02.txt'  # Pode ser alterado conforme necessário
        sentilex = carrega_lexico(caminho_arquivo_lexico)
        if not sentilex:
            return

        # Análise de sentimento
        sentimento = analyze_sentiment(sentilex)
        print("Sentimento:", sentimento)

    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro não esperado: {e}")

if __name__ == "__main__":
    main()