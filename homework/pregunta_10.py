"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
    ('A', 3, 4),
    ...
    ('E', 2, 3),
    ('E', 3, 3)]
    """
    result = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Obtenemos un arreglo con los datos de cada columna
            data = line.split()
            # Añadimos la tupla con la letra (columna 1), cantidad de elementos columna 4, cantidad de elementos columna 5
            result.append((data[0], len(data[3].split(',')), len(data[4].split(','))))

    return result