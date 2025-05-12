"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
    ('bbb', 1, 9),
    ('ccc', 1, 10),
    ('ddd', 0, 9),
    ('eee', 1, 7),
    ('fff', 0, 9),
    ('ggg', 3, 10),
    ('hhh', 0, 9),
    ('iii', 0, 9),
    ('jjj', 5, 17)]

    """
    # Aqui guardaremos cada tupla (clave, valor asociado) para luego hacer una agrupacion por clave
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Aqui tenemos un arreglo con todas las claves:valor de la linea
            data = line.split()[-1].split(',')
            for d in data:
                # Añadimos la tupla de la clave con el valor asociado
                records.append((d[:3], int(d[4:])))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = []
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):

        # Obtenemos todos los valores del grupo 
        values = [value for _, value in group]
        # Recorremos los valores de cada grupo con el min y max de la columna 2
        result.append((key, min(values), max(values)))

    return result