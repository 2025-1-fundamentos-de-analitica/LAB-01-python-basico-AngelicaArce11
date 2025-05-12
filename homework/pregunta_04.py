"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from itertools import groupby

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
    ('02', 4),
    ('03', 2),
    ('04', 4),
    ('05', 3),
    ('06', 3),
    ('07', 5),
    ('08', 6),
    ('09', 3),
    ('10', 2),
    ('11', 2),
    ('12', 3)]

    """
    # Aqui guardaremos cada tupla (mes, 1) para luego hacer una agrupacion por mes
    records = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Añadimos la tupla del mes con un uno
            records.append((line.split()[2].split('-')[1], 1))
    
    # Ordenamos el arreglo por el primer elemento de cada tupla
    records.sort(key= lambda t: t[0])

    result = []
    # Iteramos por cada clave y grupor formado --- x[0] indica que la clave es el primer elemento de cada tupla
    for key, group in groupby(records, lambda x: x[0]):
        # Recorremos los valores de cada grupo y los sumamos, ademas añadimos la tupla final (mes, cantidad)
        result.append((key, sum(value for _, value in group)))

    return result
