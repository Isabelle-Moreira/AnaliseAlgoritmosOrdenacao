import math

def shell_sort(array):
    n = len(array)
    comparations = 0
    movements = 0

    # Define o valor inicial de h
    h = 1
    while h < n:
        h = h * 3 + 1

    # Inicia a ordenação com o valor de h
    while h > 1:
        h //= 3
        for i in range(h, n):
            aux = array[i]
            movements += 1
            j = i

            comparations += 1
            while j >= h and array[j - h] > aux:
                comparations += 1
                array[j] = array[j - h]
                movements += 1
                j -= h
                if j < h:
                    break

            array[j] = aux
            movements += 1

    print(f"Comparações Empíricas: {comparations}")
    print(f"Movimentos Empíricos: {movements}")


array = [64, 25, 12, 11, 8, 6, 3, 1,0]
n = len(array)
print(f"Conjectura 1: {(math.pow(n,1.25))}")
print(f"Conjectura 2: {(n*(math.log2(n))**2)}")
shell_sort(array)
print("Array ordenado:", array)
