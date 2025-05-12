"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

    """
    # Aqui guardaremos cada tupla (clave, 1) para luego hacer una agrupacion por clave
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Aqui tenemos un arreglo con todas las claves:valor de la linea
            data = line.split()[-1].split(',')
            for d in data:
                # Añadimos la tupla de la clave con 1
                records.append((d[:3], 1))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = {}
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):
        # Añadimos la clave al diccionario con la suma 
        result[key] = sum(value for _, value in group)

    return result