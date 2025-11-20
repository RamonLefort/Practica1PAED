import tkinter as tk
from tkinter import filedialog
from weightCalculation import calculate_weight_of_task
from MergeSort import merge_sort
import time

# Función para abrir un archivo.
def ask_file():
    root = tk.Tk()
    root.withdraw()

    file_name = filedialog.askopenfilename(title="Selecciona un archivo")

    if file_name:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")

    return content

# Función para extraer los datos del archivo.
def extract_data():
    # Llamada a la función para abrir un archivo.
    content = ask_file()

    # Separación de las líneas del archivo.
    tasks = content.split("\n")
    
    # Como la primera línea del archivo es el número de tareas, se almacena en num_tasks.
    num_tasks = tasks[0]

    # Lista para almacenar los datos de las tareas.
    dictionary_tasks_parameters_list = []

    # Bucle para recorrer las líneas del archivo.
    for i in range(1, int(num_tasks) + 1):
        # Separación de los parámetros de cada tarea.
        tasks_parameters = tasks[i].split(";")

        # Separación de los parámetros de tiempo de cada tarea.
        time_parameters = tasks_parameters[1].split("-")

        # Creación de un diccionario para almacenar los parámetros de tiempo.
        dictionary_time_parameters = {
            "day": time_parameters[0],
            "month": time_parameters[1],
            "year": time_parameters[2]
        }

        # Cálculo del peso de cada tarea.
        task_weight = calculate_weight_of_task(dictionary_time_parameters["year"], dictionary_time_parameters["month"], dictionary_time_parameters["day"], tasks_parameters[5], tasks_parameters[4])

        # Creación de un diccionario para almacenar los parámetros de cada tarea.
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

        # Añadir el diccionario de parámetros de cada tarea a la lista.
        dictionary_tasks_parameters_list.append(dictionary_tasks_parameters)

    return dictionary_tasks_parameters_list
