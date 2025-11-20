import random
import string

def insertion_sort(arr, clave):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1

        while j >= 0 and arr[j][clave].lower() > key_item[clave].lower():
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_item

def generate_random_tasks(num_tasks):
    tasks = []
    for _ in range(num_tasks):
        # Generar un nombre aleatorio (entre 3 y 8 caracteres)
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(3, 8)))
        # Generar un peso aleatorio entre 1 y 200
        weight = random.randint(1, 200)
        tasks.append({"name": name, "weight": weight})
    return tasks

def test_insertion_sort_large():
    # Generar una lista más grande de tareas aleatorias
    num_tasks = 50  # Cambia este valor para aumentar/disminuir el tamaño
    tasks = generate_random_tasks(num_tasks)

    print("Lista original:")
    for task in tasks:
        print(task)

    # Ordenar la lista de diccionarios en función de "name"
    insertion_sort(tasks, "name")

    print("\nLista ordenada:")
    for task in tasks:
        print(task)

