import random

def merge(arr, i, half, j):
    aux = [0] * len(arr)
    left = i
    right = half + 1
    cursor = i

    while (left <= half) and (right <= j):
        if arr[left] <= arr[right]:
            aux[cursor] = arr[left]
            left += 1
        else:
            aux[cursor] = arr[right]
            right += 1
        cursor += 1

    while left <= half:
        aux[cursor] = arr[left]
        left += 1
        cursor += 1

    while right <= j:
        aux[cursor] = arr[right]
        right += 1
        cursor += 1

    for k in range(i, j + 1):
        arr[k] = aux[k]

def merge_sort(arr, i, j):
    if i < j:
        half = (i + j) // 2
        merge_sort(arr, i, half)
        merge_sort(arr, half + 1, j)
        merge(arr, i, half, j)

def test_merge_sort():
    numbers = []
    n = input("Introduce n para crear una array de n enteros random del 0 al 100: ")

    for i in range(0, int(n)):
        numbers.append(random.randint(0, 100))

    print("\nLa lista desordenada: ", numbers)
    merge_sort(numbers, 0, len(numbers) - 1)
    print("Lista ordenada: ", numbers)

test_merge_sort()

