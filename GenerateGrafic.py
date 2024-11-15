import time
import random
import matplotlib.pyplot as plt
from typing import List
from MergeSort import merge_sort
from QuickSort import quick_sort
import tkinter as tk
from tkinter import filedialog
from weightCalculation import calculate_weight_of_task


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


# Función mejorada `ask_file` para asegurar siempre un retorno de contenido
def ask_file():
    root = tk.Tk()
    root.withdraw()

    file_name = filedialog.askopenfilename(title="Selecciona un archivo")
    content = ""

    if file_name:
        try:
            with open(file_name, 'r') as file:
                content = file.read()
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")

    return content


# Función para medir el tiempo de ejecución de cada algoritmo en función del tamaño del array
def measure_sort_times(sizes: List[int]):
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


# Definir tamaños de arrays para la prueba hasta 500,000
sizes = [1, 100, 1000, 5000, 10000, 25000, 50000, 100000, 175000, 250000, 325000, 500000]
merge_times, quick_times = measure_sort_times(sizes)

# Graficar los resultados mejorados
# Graficar los resultados mejorados con una escala logarítmica
plt.figure(figsize=(10, 6))
plt.plot(sizes[:len(merge_times)], merge_times, label='Merge Sort', marker='o')
plt.plot(sizes[:len(quick_times)], quick_times, label='Quick Sort', marker='o')
plt.xlabel("Size of Array (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time vs. Array Size for Merge Sort and Quick Sort (Up to 500,000 Elements)")
plt.xscale('log')  # Establece la escala del eje x a logarítmica
plt.legend()
plt.grid(True)
plt.show()
