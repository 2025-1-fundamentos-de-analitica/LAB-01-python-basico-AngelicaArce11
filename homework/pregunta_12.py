"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    # Aqui guardaremos cada tupla (letra, suma de los valores de la columna 5 de cada linea) para luego hacer una agrupacion por letra
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Obtenemos un arreglo con los datos de cada linea
            data = line.split()
            # Suma valores columna 5 de la linea
            suma = 0

            # Recorremos cada elemento clave:valor de la columna 5
            for d in data[4].split(','):
                suma += int(d[4:])

            # Añadimos la tupla con la letra y la suma correspondiente a esa linea
            records.append((data[0], suma))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = {}
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):
        # Añadimos la clave (letra) al diccionario con la suma (valores columna5 de todo el documento)
        result[key] = sum(value for _, value in group)

    return result