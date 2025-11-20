# Función para ordenar una lista de diccionarios utilizando el algoritmo de Insertion Sort.
# El parámetro key es el que se utilizará para ordenar la lista.
# Se considera que siempre se introducirá un diccionario y que la clave siempre existirá y sera un string.
def insertion_sort(arr, key='name'):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j][key].lower() < arr[j-1][key].lower():
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

# Prueba del algoritmo
def test_insertion_sort():
    tasks = [
        {"name": "AAABBB", "weight": 5},
        {"name": "AAAABB", "weight": 12},
        {"name": "ZZZSS", "weight": 32},
        {"name": "Task B", "weight": 2},
        {"name": "C", "weight": 3},
        {"name": "ZZZZZ", "weight": 1},
        {"name": "Task D", "weight": 35},
        {"name": "Task E", "weight": 155},
        {"name": "Task F", "weight": 43},
        {"name": "ZZZZZ", "weight": 23},
    ]

    print("Lista original:")
    for task in tasks:
        print(task)

    # Aplicar Insertion Sort
    insertion_sort(tasks, "name")

    print("\nLista ordenada:")
    for task in tasks:
        print(task)

# test_insertion_sort()
