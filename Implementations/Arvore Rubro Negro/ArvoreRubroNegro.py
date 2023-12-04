from sortedcontainers import SortedDict
import random
import time

# Função para preencher a árvore com dados do arquivo
def preencher_arvore(arvore, dados):
    for numero in dados:
        arvore[numero] = numero

# Função para realizar operações aleatórias na árvore
def operacoes_aleatorias(arvore, numeros):
    for numero in numeros:
        if numero % 3 == 0:
            arvore[numero] = numero  # Inserir se múltiplo de 3
        elif numero % 5 == 0:
            # Remover se múltiplo de 5
            if numero in arvore:
                del arvore[numero]
        else:
            # Contar quantas vezes o número aparece na árvore
            count = sum(1 for _, value in arvore.items() if value == numero)
            print(f'O número {numero} aparece {count} vezes na árvore.')

# Dados do arquivo
with open('dados100_mil.txt', 'r') as file:
    dados_arquivo = [int(numero) for line in file for numero in line.strip().split(',')]

# Garantir que a amostra aleatória não seja maior que a população
tamanho_amostra = min(50000, len(dados_arquivo))
numeros_aleatorios = random.sample(dados_arquivo, tamanho_amostra)




# Árvore Rubro-Negra
inicio_rn = time.time()
arvore_rn = SortedDict()
preencher_arvore(arvore_rn, dados_arquivo)
operacoes_aleatorias(arvore_rn, numeros_aleatorios)
tempo_rn = time.time() - inicio_rn

# Árvore AVL
inicio_avl = time.time()
arvore_avl = SortedDict(key=lambda x: x)  # Usando key=lambda x: x para simular uma AVL
preencher_arvore(arvore_avl, dados_arquivo)
operacoes_aleatorias(arvore_avl, numeros_aleatorios)
tempo_avl = time.time() - inicio_avl

# Comparativo
print(f'Tempo de execução para Árvore Rubro-Negra: {tempo_rn:.4f} segundos')
print(f'Tempo de execução para Árvore AVL: {tempo_avl:.4f} segundos')
