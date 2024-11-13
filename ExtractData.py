import tkinter as tk
from tkinter import filedialog
from weightCalculation import calculate_weight_of_task
from MergeSort import merge_sort
import time

def extract_data():
    root = tk.Tk()
    root.withdraw()

    file_name = filedialog.askopenfilename(title="Selecciona un archivo")

    if file_name:
        try:
            with open(file_name, 'r') as file:
                content = file.read()
        except Exception as e:
            print(f"Ocurrió un error al abrir el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")


    tasks = content.split("\n")
    # num_tasks = tasks[0]
    num_tasks = 300000

    dictionary_tasks_parameters_list = []

    for i in range(1, int(num_tasks) + 1):
        tasks_parameters = tasks[i].split(";")
        time_parameters = tasks_parameters[1].split("-")
        dictionary_time_parameters = {
            "day": time_parameters[0],
            "month": time_parameters[1],
            "year": time_parameters[2]
        }

        task_weight = calculate_weight_of_task(dictionary_time_parameters["year"], dictionary_time_parameters["month"], dictionary_time_parameters["day"], tasks_parameters[5], tasks_parameters[4])

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

dictionary_tasks_parameters_list = extract_data()

print("Data extracted")

starting_time = time.time()
merge_sort(dictionary_tasks_parameters_list, 0, len(dictionary_tasks_parameters_list) - 1, "weight")
ending_time = time.time()

elapsed_time_seconds = ending_time - starting_time
elapsed_time_minutes = elapsed_time_seconds / 60

for (i, task_dictionary) in enumerate(dictionary_tasks_parameters_list):
    print(i, f"Task: {task_dictionary["name"]}")
    print(f"\t{task_dictionary["weight"]}")


print("Tiempo de ejecución de mergeSort:", elapsed_time_seconds, "segundos")
print("Tiempo de ejecución de mergeSort:", elapsed_time_minutes, "minutos")