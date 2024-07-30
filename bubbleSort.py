def bubble_sort(array):
    mComparations = 0
    mMoviments = 0
    n = len(array)
    
    # Bubble Sort 
    for i in range(n - 1):
        for j in range(1, n - i):
            mComparations += 1
            if array[j] < array[j - 1]:
                #troca elementos
                mMoviments += 3
                array[j], array[j - 1] = array[j - 1], array[j]
    
    
    return mComparations, mMoviments


items = [100,20,15,13,12,11,5,4,1]
n = len(items)
# Performando o Bubble sort
comparations, movements = bubble_sort(items)

#Formula teorica
formulaComparacao = ((n*(n-1))/2)
formulaMovimentacao = 3*((n*(n-1))/2)


# Printando os items da analise do bubble
print("Sorted items:", items)
print("Empiric Comparations:", comparations)
print("Teoric Comparations", formulaComparacao)
print("Moviments:", movements)
print("Teoric Moviments", formulaMovimentacao)

