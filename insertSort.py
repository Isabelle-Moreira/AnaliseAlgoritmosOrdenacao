def insertion_sort(array):
    comparisons = 0  # Variável local para comparações
    movements = 0    # Variável local para movimentos
    
    n = len(array)
    for i in range(1, n):
        aux = array[i]
        movements += 1
        j = i - 1
        
        while j >= 0 and aux < array[j]:
            comparisons += 1
            array[j + 1] = array[j]
            movements += 1
            j -= 1
        
        array[j + 1] = aux
        movements += 1

    print_stats(comparisons, movements)


def print_stats(comparisons, movements):
    print(f"Comparação empiricas: {comparisons}")
    print(f"Movimentos empiricos: {movements}")

a = [8,7,5,4,1]
n = len(a)

print(f"Comparação teorica: {((n*n)-n)/2}")
print(f"Movimentos teorica: {((n*n)+(3*n)-4)/2}")

insertion_sort(a)
print("Sorted array:", a)
