import time
import random
import matplotlib.pyplot as plt
from typing import List

from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
import tkinter as tk
from tkinter import filedialog

from SelectionSort import selection_sort
from weightCalculation import calculate_weight_of_task



# Función extract_data modificada para poder elegir el número de iteraciones.
def extract_data(iterations, content):
    tasks = content.split("\n")

    dictionary_tasks_parameters_list = []

    for i in range(1, int(iterations) + 1):
        tasks_parameters = tasks[i].split(";")
        time_parameters = tasks_parameters[1].split("-")

        dictionary_time_parameters = {
            "day": time_parameters[0],
            "month": time_parameters[1],
            "year": time_parameters[2]
        }

        task_weight = calculate_weight_of_task(
            dictionary_time_parameters["year"],
            dictionary_time_parameters["month"],
            dictionary_time_parameters["day"],
            tasks_parameters[5],
            tasks_parameters[4]
        )

        # Crear el diccionario de parámetros
        dictionary_tasks_parameters = {
            "name": tasks_parameters[0],
            "date": tasks_parameters[1],
            "time": dictionary_time_parameters,
            "difficulty": tasks_parameters[3],
            "progress": tasks_parameters[4],
            "importance": tasks_parameters[5],
            "building": tasks_parameters[6],
            "weight": task_weight
        }

        dictionary_tasks_parameters_list.append(dictionary_tasks_parameters)

    return dictionary_tasks_parameters_list


# Función auxiliar para abrir el archivo.
def ask_file():
    root = tk.Tk()
    root.withdraw()

    file_name = filedialog.askopenfilename(title="Selecciona un archivo")
    content = ""

    if file_name:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")

    return content


# Función para calcular los tiempos de ejecución de los algoritmos recursivos (Merge Sort y Quick Sort).
# Recibe como parámetro una lista con los tamaños de las iteraciones.
def measure_recursive_sort_times(sizes: List[int]):
    merge_times = []
    quick_times = []

    content = ask_file()

    for size in sizes:
        try:
            dictionary_tasks_parameters_list = extract_data(size, content)
        except ValueError as e:
            print(e)
            break

        aux = [None] * len(dictionary_tasks_parameters_list)

        start_time = time.time()
        merge_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight", aux)
        merge_times.append(time.time() - start_time)

        start_time = time.time()
        quick_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight")
        quick_times.append(time.time() - start_time)

    return merge_times, quick_times

# Función para calcular los tiempos de ejecución de los algoritmos iterativos (Insertion Sort y Selection Sort).
# Recibe como parámetro una lista con los tamaños de las iteraciones.
def measure_iterative_sort_times(sizes: List[int]):
    insertion_times = []
    selection_times = []

    content = ask_file()

    for size in sizes:
        try:
            dictionary_tasks_parameters_list = extract_data(size, content)
        except ValueError as e:
            print(e)
            break

        start_time = time.time()
        insertion_sort(dictionary_tasks_parameters_list, "name")
        insertion_times.append(time.time() - start_time)

        start_time = time.time()
        selection_sort(dictionary_tasks_parameters_list, "name")
        selection_times.append(time.time() - start_time)

    return insertion_times, selection_times

# Función para calcular los tiempos de ejecución de Insertion Sort.
# Recibe como parámetro una lista con los tamaños de las iteraciones.
def measure_insertion_sort_times(sizes: List[int]):
    insertion_times = []

    content = ask_file()

    for size in sizes:
        try:
            dictionary_tasks_parameters_list = extract_data(size, content)
        except ValueError as e:
            print(e)
            break

        start_time = time.time()
        insertion_sort(dictionary_tasks_parameters_list, "name")
        insertion_times.append(time.time() - start_time)

    return insertion_times

# Función para graficar los tiempos de ejecución de los algoritmos recursivos (Merge Sort y Quick Sort).
def recursive_algorithm_graph():
    # Tamaños de las iteraciones.
    # Si quieres graficar para diferentes tamaños de input modifica la lista.
    sizes = [1, 100, 1000, 5000, 10000, 25000, 50000, 100000, 175000, 250000, 325000, 500000]


    merge_times, quick_times = measure_recursive_sort_times(sizes)

    # Uso de la librería matplotlib para graficar los resultados.
    plt.figure(figsize=(10, 6))

    # Para el eje x utilizamos la lista sizes, haciendole un slicing de la longitud tanto de Merge como de Quick Sort.
    # Para el eje y utilizamos la lista de tiempos de cada uno de los algoritmos.
    plt.plot(sizes[:len(merge_times)], merge_times, label='Merge Sort', marker='o')
    plt.plot(sizes[:len(quick_times)], quick_times, label='Quick Sort', marker='o')

    plt.xlabel("Size of Array (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs. Array Size for Merge Sort and Quick Sort (Up to 500,000 Elements)")
    plt.xscale('log')  
    plt.legend()
    plt.grid(True)
    plt.show()


def iterative_algorithm_graph():
    # Tamaños de las iteraciones.
    # Si quieres graficar para diferentes tamaños de input modifica la lista.
    sizes = [1, 100, 1000, 5000, 10000, 20000]

    insertion_times, selection_times = measure_iterative_sort_times(sizes)

    # Uso de la librería matplotlib para graficar los resultados.
    plt.figure(figsize=(10, 6))

    # Para el eje x utilizamos la lista sizes, haciendole un slicing de la longitud tanto de Merge como de Quick Sort.
    # Para el eje y utilizamos la lista de tiempos de cada uno de los algoritmos.
    plt.plot(sizes[:len(insertion_times)], insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes[:len(selection_times)], selection_times, label='Selection Sort', marker='o')
    plt.xlabel("Size of Array (n)", fontsize=12)
    plt.ylabel("Execution Time (seconds)", fontsize=12)
    plt.title("Execution Time vs. Array Size for Insertion Sort and Selection Sort", fontsize=14)
    plt.xscale('log')  
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def insertion_sort_graph():
    # Tamaños de las iteraciones.
    # Si quieres graficar para diferentes tamaños de input modifica la lista.
    sizes = [1, 100, 1000, 5000, 10000, 25000, 50000, 100000, 175000, 250000, 325000, 500000]

    insertion_times = measure_insertion_sort_times(sizes)

    # Uso de la librería matplotlib para graficar los resultados.
    plt.figure(figsize=(10, 6))

    # Para el eje x utilizamos la lista sizes.
    # Para el eje y utilizamos la lista de tiempos de cada uno de los algoritmos.
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.xlabel("Size of Array (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time vs. Array Size for Insertion Sort")
    plt.xscale('log')
    plt.legend()
    plt.grid(True)
    plt.show()


recursive_algorithm_graph()
