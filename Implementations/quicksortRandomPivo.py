import random
import time

def gerar_lista_aleatoria(n, min_valor, max_valor):
    return [random.randint(min_valor, max_valor) for _ in range(n)]

def quick_sort(arr):
    # Função auxiliar para contar os movimentos
    def partition(arr, low, high):
        # Escolhe um índice aleatório entre low e high
        random_index = random.randint(low, high)
        # Troca o elemento aleatório com o último elemento para torná-lo o pivô
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot = arr[high]
        i = low - 1
        moves = 0  # Inicializa a contagem de movimentos em 0

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Troca arr[i] e arr[j]
                moves += 1  # Incrementa a contagem de movimentos

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Troca arr[i+1] e o pivô
        moves += 1  # Incrementa a contagem de movimentos

        return i + 1, moves

    # Função principal de ordenação Quick Sort
    def quick_sort_helper(arr, low, high):
        moves = 0  # Inicializa a contagem de movimentos em 0

        if low < high:
            pivot_index, partition_moves = partition(arr, low, high)
            moves += partition_moves  # Adiciona os movimentos da partição atual

            # Recursivamente ordena os elementos antes e depois do pivô
            moves += quick_sort_helper(arr, low, pivot_index - 1)
            moves += quick_sort_helper(arr, pivot_index + 1, high)

        return moves

    # Chama a função principal com os índices iniciais
    total_moves = quick_sort_helper(arr, 0, len(arr) - 1)

    return arr, total_moves

print('Digite quantos números deseja ordenar: ')
n = int(input())
min_valor = 1
max_valor = 999999

# Registre o tempo de início
start_time = time.time()

arr = gerar_lista_aleatoria(n, min_valor, max_valor)
print('Lista aleatória: ', arr)
sorted_arr, moves = quick_sort(arr)
print('Array ordenado:', sorted_arr)
print('Total de movimentos:', moves)

# Registre o tempo de término
end_time = time.time()

# Calcule a diferença de tempo em segundos
elapsed_time_seconds = end_time - start_time

# Converta para o formato HH:MM:SS:mm
elapsed_time_minutes, elapsed_time_seconds = divmod(int(elapsed_time_seconds), 60)
elapsed_time_hours, elapsed_time_minutes = divmod(elapsed_time_minutes, 60)
elapsed_time_hours, elapsed_time_minutes = divmod(elapsed_time_minutes, 60)

print(f'Tempo decorrido: {elapsed_time_hours:02d}:{elapsed_time_minutes:02d}:{elapsed_time_seconds:02d}:{int((elapsed_time_seconds - int(elapsed_time_seconds)) * 1000):03d}')
