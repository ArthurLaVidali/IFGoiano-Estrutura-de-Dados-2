import random
import time

def gerar_lista_aleatoria(n, min_valor, max_valor):
    return [random.randint(min_valor, max_valor) for _ in range(n)]

def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        moves = 0

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                moves += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        moves += 1

        return i + 1, moves

    def quick_sort_helper(arr, low, high):
        moves = 0

        if low < high:
            pivot_index, partition_moves = partition(arr, low, high)
            moves += partition_moves

            moves += quick_sort_helper(arr, low, pivot_index - 1)
            moves += quick_sort_helper(arr, pivot_index + 1, high)

        return moves

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
