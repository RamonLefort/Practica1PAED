import time
from ExtractData import extract_data
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from SelectionSort import selection_sort


# Extraemos los datos del archivo.
dictionary_tasks_parameters_list = extract_data()
print("Data extracted")

# Creamos la array auxiliar.
aux = [None] * len(dictionary_tasks_parameters_list) 

# Función para ordenar la lista con Merge Sort.
def order_with_merge_sort():

    starting_time = time.time()
    merge_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight", aux)
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Mostrar lista ordenada.
    # Si quieres comprobar el correcto funcionamiento, descomenta el siguiente bloque de código.
    """for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")
        print(f"\t{task_dictionary["weight"]}")"""

    print("\nSorted with MergeSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

# Función para ordenar la lista con Quick Sort.
def order_with_quick_sort():

    starting_time = time.time()
    quick_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight")
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Mostrar lista ordenada.
    # Si quieres comprobar el correcto funcionamiento, descomenta el siguiente bloque de código.
    """for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")
        print(f"\t{task_dictionary["weight"]}")"""

    print("\nSorted with QuickSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

# Función para ordenar la lista con Insertion Sort.
def order_with_insertion_sort():

    starting_time = time.time()
    insertion_sort(dictionary_tasks_parameters_list, "name")
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Si quieres comprobar el correcto funcionamiento, descomenta el siguiente bloque de código.
    """for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")"""

    print("\nSorted with InsertionSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

# Función para ordenar la lista con Selection Sort.
def order_with_selection_sort():
    starting_time = time.time()
    selection_sort(dictionary_tasks_parameters_list, "name")
    ending_time = time.time()

    elapsed_time_seconds = ending_time - starting_time
    elapsed_time_minutes = elapsed_time_seconds / 60

    # Si quieres comprobar el correcto funcionamiento, descomenta el siguiente bloque de código.
    """for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
        print(i, f"Task: {task_dictionary["name"]}")"""

    print("\nSorted with SelectionSort")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
    print("\tTiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")

order_with_insertion_sort()