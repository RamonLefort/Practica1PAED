import math
from datetime import datetime

def calculate_time_weight(limit_year, limit_month, limit_day):
    # Hacemos un try para el caso que te introduzca una fecha anterior a la actual.
    actual_date = datetime.now().date()  # Fecha actual sin hora
    limit_date = datetime(2000 + limit_year, limit_month, limit_day).date()  # Fecha límite sin hora

    delta_days = max((limit_date - actual_date).days, 1)

    return min(int(1000 / (delta_days ** 0.5)), 500)



def calculate_red_weight_by_hexa(color):
    color = color.lstrip('#')

    rgb = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
    return rgb[0]



def calculate_weight_of_task(limit_year, limit_month, limit_day, color, progress):
    time_weight = calculate_time_weight(int(limit_year), int(limit_month), int(limit_day))
    red_weight = calculate_red_weight_by_hexa(color)

    return int(time_weight) + int(red_weight) + int(progress)


# Ejemplo de uso


