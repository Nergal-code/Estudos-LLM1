import random
import itertools

# Texto de amostra para a fase de "treinamento"
texto = """
Inteligência artificial e aprendizado de máquina são campos de estudo que estão crescendo rapidamente. 
As possibilidades são infinitas, e o impacto no futuro é imenso.
Inteligência artificial está remodelando a maneira como pensamos, trabalhamos e vivemos.
"""

# Tokenização: dividindo o texto em palavras
palavras = texto.split()

# Construir um dicionário de trigramas (triplas de palavras)
trigramas = {}

for i in range(len(palavras) - 2):
    tripla_palavras = (palavras[i], palavras[i + 1], palavras[i + 2])
    if tripla_palavras in trigramas:
        trigramas[tripla_palavras] += 1
    else:
        trigramas[tripla_palavras] = 1

# Gerar uma frase com base nos trigramas
def gerar_frase(palavra_inicial, comprimento=10):
    # Encontrar todos os trigramas que começam com a palavra dada
    trigramas_candidatos = [tripla for tripla in trigramas if tripla[0] == palavra_inicial]

    if not trigramas_candidatos:
        return f"Não é possível gerar uma frase começando com '{palavra_inicial}'"

    tripla_atual = random.choices(trigramas_candidatos, weights=[trigramas[t] for t in trigramas_candidatos])[0]
    frase = list(tripla_atual[:2])  # Iniciar a frase com as duas primeiras palavras da tripla escolhida

    for _ in range(comprimento - 2):
        proximas_palavras_candidatas = [(tripla[2], trigramas[tripla]) for tripla in trigramas if tripla[:2] == tuple(frase[-2:])]
        
        if not proximas_palavras_candidatas:
            break
        
        # Seleção aleatória ponderada da próxima palavra com base na frequência
        proxima_palavra = random.choices(
            [palavra for palavra, _ in proximas_palavras_candidatas],
            weights=[peso for _, peso in proximas_palavras_candidatas]
        )[0]
        
        frase.append(proxima_palavra)
    
    return ' '.join(frase)

# Obter entrada do usuário para a palavra inicial e comprimento da frase
palavra_inicial = input("Digite uma palavra inicial: ")
comprimento_frase = int(input("Digite o comprimento da frase (número de palavras): "))

# Verificar se a palavra inicial está na lista de palavras
if palavra_inicial not in palavras:
    print(f"'{palavra_inicial}' não encontrada no texto, escolhendo uma palavra aleatória.")
    palavra_inicial = random.choice(palavras)

# Gerar e imprimir a frase
frase_gerada = gerar_frase(palavra_inicial, comprimento=comprimento_frase)
print("Frase gerada:", frase_gerada)

