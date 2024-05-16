Análise de Sentimento

Este é um projeto de análise de sentimento que identifica se um determinado comentário é positivo, negativo ou neutro com base em um conjunto de palavras definidas.

### Como Funciona

O projeto utiliza uma abordagem simples de correspondência de palavras-chave. Ele divide um comentário em palavras individuais, verifica se essas palavras estão em listas predefinidas de palavras positivas e negativas, e então determina o sentimento com base na contagem de ocorrências de palavras positivas e negativas.

### Uso

Instalação das Dependências: Antes de usar o projeto, é necessário ter o Python instalado no seu sistema. Além disso, é necessário instalar o módulo nltk para manipulação de texto. Você pode instalar as dependências executando o seguinte comando:

bash
Copiar código
pip install nltk
Execução do Projeto: Após instalar as dependências, execute o arquivo analyze_sentiment.py. Isso iniciará o programa, que solicitará um comentário de entrada. Após inserir o comentário, o programa determinará se é positivo, negativo ou neutro.

bash
Copiar código
python analyze_sentiment.py
Adaptação para Português: O projeto atual utiliza um conjunto de palavras positivas e negativas em inglês. Se desejar adaptá-lo para o português, você pode criar seus próprios arquivos de palavras positivas e negativas e atualizar o código conforme necessário.

### Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Autora

Kim Gomes
