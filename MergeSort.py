import random

def merge(arr, i, half, j):
    # Crear una lista auxiliar del mismo tamaño que arr
    aux = [0] * len(arr)
    left = i
    right = half + 1
    cursor = i

    # Mezclar los elementos desde las dos mitades
    while (left <= half) and (right <= j):
        if arr[left] <= arr[right]:
            aux[cursor] = arr[left]
            left += 1
        else:
            aux[cursor] = arr[right]
            right += 1
        cursor += 1

    # Copiar los elementos restantes de la mitad izquierda (si los hay)
    while left <= half:
        aux[cursor] = arr[left]
        left += 1
        cursor += 1

    # Copiar los elementos restantes de la mitad derecha (si los hay)
    while right <= j:
        aux[cursor] = arr[right]
        right += 1
        cursor += 1

    # Copiar los elementos ordenados de la lista auxiliar a la original
    for k in range(i, j + 1):
        arr[k] = aux[k]

def mergeSort(arr, i, j):
    if i < j:
        half = (i + j) // 2
        mergeSort(arr, i, half)
        mergeSort(arr, half + 1, j)
        merge(arr, i, half, j)

def testMergeSort():
    numbers = []
    n = input("Introduce n para crear una array de n enteros random del 0 al 100: ")

    for i in range(0, int(n)):
        numbers.append(random.randint(0, 100))

    print("\nLa lista desordenada: ", numbers)
    mergeSort(numbers, 0, len(numbers) - 1)
    print("Lista ordenada: ", numbers)

testMergeSort()

