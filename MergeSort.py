def merge(arr, i, half, j, key):
    # Crear una lista auxiliar
    aux = [None] * len(arr)
    left = i
    right = half + 1
    cursor = i

    # Mezclar los elementos desde las dos mitades, comparando por la clave especificada en `key`
    while left <= half and right <= j:
        if arr[left][key] <= arr[right][key]:
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

def merge_sort(arr, i, j, key):
    if i < j:
        half = (i + j) // 2
        merge_sort(arr, i, half, key)
        merge_sort(arr, half + 1, j, key)
        merge(arr, i, half, j, key)

# Ejemplo de uso
def merge_sort_test():
    tasks = [
        {"name": "Task A", "weight": 5},
        {"name": "Task B", "weight": 2},
        {"name": "Task C", "weight": 3},
        {"name": "Task D", "weight": 1}
    ]

    # Ordenar la lista de diccionarios en función de "weight"
    merge_sort(tasks, 0, len(tasks) - 1, "weight")

    # Imprimir la lista ordenada
    for task in tasks:
        print(task)
