# Función para ordenar una lista de diccionarios utilizando el algoritmo de Selection Sort.
# Presupone que le llegará una lista de diccionarios y que la clave siempre existirá y el valor de la clave sera un string.
def selection_sort(arr, key='name'):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][key].lower() < arr[min_idx][key].lower():
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def test_selection_sort():
    arr = [
        {'name': 'Carlos', 'weight': 70},
        {'name': 'Ana', 'weight': 55},
        {'name': 'Elena', 'weight': 60},
        {'name': 'Pedro', 'weight': 80}
    ]
    print("Lista original:", arr)
    selection_sort(arr)
    print("Lista ordenada por nombre:")
    for item in arr:
        print(item)

# test_selection_sort()

