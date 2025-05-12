"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # Aqui guardaremos cada tupla (letra, 1) para luego hacer una agrupacion por letra
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Añadimos la tupla de la letra con un uno
            records.append((line.split()[0], 1))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = []
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):
        # Recorremos los valores de cada grupo y los sumamos, ademas añadimos la tupla final (letra, cantidad)
        result.append((key, sum(value for _, value in group)))

    return result