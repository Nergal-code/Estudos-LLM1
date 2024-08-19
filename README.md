# Modelo Básico de Linguagem

Este é um modelo de linguagem muito simples implementado em Python. Ele usa tokenização e frequência de trigramas para gerar novas frases com base no texto de amostra fornecido.

## Visão Geral do Projeto

Este projeto demonstra uma introdução básica à construção de um modelo de linguagem usando Python. Ele recebe um texto de amostra, divide-o em palavras individuais e cria um dicionário de frequência de trigramas. Com base neste dicionário, o modelo gera uma frase escolhendo palavras de forma ponderada.

## Como Funciona

1. **Tokenização**: O texto de entrada é dividido em palavras individuais.
2. **Frequência de Trigramas**: O modelo constrói uma tabela de frequência de triplas de palavras (trigramas).
3. **Geração de Frases**: Uma nova frase é gerada com base nos trigramas, onde cada palavra é escolhida de forma ponderada de acordo com sua frequência.

## Exemplo

Aqui está um exemplo de como o modelo pode gerar uma frase:


## Uso

Para executar o projeto:

1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o arquivo `modelo_linguagem.py` e execute-o usando Python:
    ```bash
    python modelo_linguagem.py
    ```
3. O script gerará uma frase aleatória com base no texto fornecido.

## Licença

Este projeto é de código aberto sob a Licença MIT.

---

Feito por Nergal-code / Caio Lima
