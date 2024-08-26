def select_sort(array):
    n = len(array)
    comparations = 0
    movements = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparations += 1
            if array[j] < array[min_index]:
                min_index = j

        aux = array[min_index]
        movements += 1
        array[min_index] = array[i]
        movements += 1
        array[i] = aux
        movements += 1

    print(f"Comparações Empíricas: {comparations}")
    print(f"Movimentos Empíricos: {movements}")

array = [64, 25, 12,8,1]
n = len(array)

select_sort(array)
print(f"Comparações Teóricas: {((n * n) - n) / 2}")
print(f"Movimentos Teóricos: {3 * n - 3}")
print("Array ordenado:", array)
