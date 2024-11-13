def merge(arr, i, half, j, key, aux):
    # Crear una lista auxiliar
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

def merge_sort(arr, i, j, key, aux):
    if i < j:
        half = (i + j) // 2
        merge_sort(arr, i, half, key, aux)
        merge_sort(arr, half + 1, j, key, aux)
        merge(arr, i, half, j, key, aux)

# Ejemplo de uso
def merge_sort_test():
    tasks = [
        {"name": "Task A", "weight": 5},
        {"name": "Task B", "weight": 2},
        {"name": "Task C", "weight": 3},
        {"name": "Task D", "weight": 1},
        {"name": "Task E", "weight": 12},
        {"name": "Task F", "weight": 23},
        {"name": "Task G", "weight": 32},
        {"name": "Task D", "weight": 35},
        {"name": "Task E", "weight": 155},
        {"name": "Task F", "weight": 43},
    ]

    # Ordenar la lista de diccionarios en función de "weight"
    aux = [None] * len(tasks)
    merge_sort(tasks, 0, len(tasks) - 1, "weight", aux)

    # Imprimir la lista ordenada
    for task in tasks:
        print(task)

# merge_sort_test()