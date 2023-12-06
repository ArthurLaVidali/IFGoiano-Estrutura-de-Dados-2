import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers_str = file.read().replace('[', '').replace(']', '').split(',')
        return [int(num) for num in numbers_str]

if __name__ == "__main__":
    file_path = 'dados100_mil.txt'  

    # Leitura dos números do arquivo
    numbers = read_numbers_from_file(file_path)

    # Medição do tempo de execução do Quick Sort
    start_time = time.time()
    sorted_numbers = quick_sort(numbers)
    end_time = time.time()

    # Cálculo e exibição do tempo de execução
    execution_time = end_time - start_time

    print("Números ordenados:", sorted_numbers)
    
    print(f"Tempo de execução do Quick Sort: {execution_time:.3f} segundos")
