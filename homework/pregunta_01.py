"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214

    """
    # Aqui almacenamos los valores de la segunda columna
    columnValues = []

    # Abrimos el archivo y leemos linea por linea
    with open('files/input/data.csv', "r", encoding="utf-8") as f:
        for line in f:
            # Obtenemos el valor de la segunda columna
            columnValues.append(int(line.split()[1]))
    
    # Devolvemos la suma de todos los valores
    return sum(columnValues)