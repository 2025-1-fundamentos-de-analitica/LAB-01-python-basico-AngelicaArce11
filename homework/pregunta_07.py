"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
    (1, ['E', 'B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E', 'E', 'D']),
    (4, ['E', 'B']),
    (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
    (6, ['C', 'E', 'A', 'B']),
    (7, ['A', 'C', 'E', 'D']),
    (8, ['E', 'D', 'E', 'A', 'B']),
    (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """

    # Aqui guardaremos cada tupla (valor columna 2, valor columna 1) para luego hacer una agrupacion por el valor de la columna 2
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Añadimos la tupla del valor columna 2 con el valor columna 1 (letra)
            records.append((int(line.split()[1]), line.split()[0]))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = []
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):

        # Obtenemos todos los valores del grupo --- las letras 
        values = [value for _, value in group]
        # Añadimos la tupla final con el valor de la columna 2 y el arreglo de letras
        result.append((key, values))

    return result