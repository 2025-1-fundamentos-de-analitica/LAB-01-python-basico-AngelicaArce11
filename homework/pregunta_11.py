"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    # Aqui guardaremos cada tupla (letra columna 4, valor columna 2) para luego hacer una agrupacion por letra
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Obtenemos un arreglo con los datos de cada linea
            data = line.split()

            # Recorremos cada letra de la columna 4
            for d in data[3].split(','):
                # Añadimos la tupla con la letra y el valor de la columna 2
                records.append((d, int(data[1])))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = {}
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):
        # Añadimos la clave (letra) al diccionario con la suma (valores columna2)
        result[key] = sum(value for _, value in group)

    return result