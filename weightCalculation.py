import math
from datetime import datetime

def calculate_time_weight(limit_year, limit_month, limit_day):
    actual_date = datetime.now().date()  # Fecha actual sin hora
    limit_date = datetime(2000 + limit_year, limit_month, limit_day).date()  # Fecha límite sin hora

    delta_days = max((limit_date - actual_date).days, 1)  # Evitamos división por cero

    return min(int(1000 / (delta_days ** 0.5)), 500)  # Equivalente a 1000 / (delta_days)^(1/2)

def calculate_red_weight_by_hexa(color):
    color = color.lstrip('#')

    rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
    return rgb[0]



def calculate_weight_of_task(limit_year, limit_month, limit_day, color, progress):
    time_weight = calculate_time_weight(limit_year, limit_month, limit_day)
    red_weight = calculate_red_weight_by_hexa(color)

    return time_weight + red_weight + progress


# Ejemplo de uso
