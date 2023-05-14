"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    sum = 0
    for i in data:
        sum += int(i[1])
    return sum

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return


def pregunta_02():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic = {}
    tupleList = []

    for i in data:
        if i[0] in dic:
            dic[i[0]] += 1
        else:
            dic[i[0]] = 1
    for i in dic:
        tupleList.append(tuple([i, dic[i]]))
    tupleList = sorted(tupleList)
    return tupleList

    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """


def pregunta_03():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic = {}
    tupleList = []

    for line in data:
        if line[0] in dic:
            dic[line[0]] += int(line[1])
        else:
            dic[line[0]] = int(line[1])
    for char in dic:
        tupleList.append(tuple([char, dic[char]]))
    tupleList = sorted(tupleList)
    return tupleList 

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """


def pregunta_04():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic = {}
    tupleList = []

    for line in data:
        month = line[2].split("-")[1]
        if month in dic:
            dic[month] += 1
        else:
            dic[month] = 1
    for month in dic:
        tupleList.append(tuple([month, dic[month]]))
    tupleList = sorted(tupleList)
    return tupleList

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """


def pregunta_05():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic = {}
    tupleList = []

    for line in data:
        if line[0] in dic:
            dic[line[0]][0] = max(dic[line[0]][0], int(line[1]))
            dic[line[0]][1] = min(dic[line[0]][1], int(line[1]))
        else:
            dic[line[0]] = [int(line[1]), int(line[1])]
    for char in dic:
        tupleList.append(tuple([char, dic[char][0], dic[char][1]]))
    tupleList = sorted(tupleList)
    return tupleList

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return


def pregunta_06():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic, tupleList = {}, []

    for i in range(len(data)):
        dictColum = data[i][4]
        dictList = dictColum.split(",")
        keyValueList = [element.split(":") for element in dictList]
        dictionary = {element[0]: element[1] for element in keyValueList}

        for j in dictionary:
            if j in dic:
                dic[j][0] = max(int(dic[j][0]), int(dictionary[j]))
                dic[j][1] = min(int(dic[j][1]), int(dictionary[j]))
            else:
                dic[j] = [int(dictionary[j]), int(dictionary[j])]

    for i in dic:
        tupleList.append(tuple([i, dic[i][1], dic[i][0]]))
    tupleList = sorted(tupleList)
    return tupleList

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

def pregunta_07():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic, tupleList = {}, []
    
    for line in data:
        num = line[1]
        char = line[0]
        if num in dic:
            dic[num] += [char]
        else:
            dic[num] = [char]
    for i in dic:
        tupleList.append(tuple([int(i), dic[i]]))
    tupleList = sorted(tupleList)
    return tupleList
#esta pregunta nos esta dando un error y no sabemos identificarlo puesto que nos da la salida correcta pero puede que este fallando en algun parametro 

"""
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

def pregunta_08():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic, tupleList = {}, []
    
    for line in data:
        num = line[1]
        char = line[0]
        if num in dic:
            dic[num] += char
        else:
            dic[num] = [char]
    for i in dic:
        tupleList.append(tuple([int(i), sorted(list(set(dic[i])))]))
    tupleList = sorted(tupleList)
    return tupleList
#esta pregunta nos esta dando un fallo y no sabemos explicar el porque? 
#pedir asesoria al profesor o buscar a sebastian para posibles fallos en el codigo 
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

def pregunta_09():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic, dic2  = {}, {}

    for key in range(len(data)):
        dictColum = data[key][4]
        dictionaries = dictColum.split(",")
        keyValueList = [element.split(":") for element in dictionaries]
        dictionary = {element[0]: element[1] for element in keyValueList}
        for key in dictionary:
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
    for key in sorted(dic):
        dic2[key] = dic[key]
    return dic2

    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

def pregunta_10():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    tupleList = []

    for line in data:
        char = line[0]
        elements = line[3]
        dicts = line[4]

        elementCount = len(elements.split(","))
        dictCount = len(dicts.split(","))
        tupleList.append(tuple([char, elementCount, dictCount]))
    return tupleList

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

def pregunta_11():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic, dic2 = {}, {}

    for line in data:
        chars = line[3].split(",")
        value = line[1]
        for char in chars:
            if char in dic:
                dic[char] += int(value)
            else:
                dic[char] = int(value)
    for char in sorted(dic):
        dic2[char] = dic[char]
    return dic2

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

def pregunta_12():
    with open("data.csv", "r") as file:
        data = file.readlines()
    data = [i.split("\t") for i in data]

    dic, dic2 = {}, {}

    for line in data:
        char = line[0]
        dictColum = line[4]
        dictList = dictColum.split(",")
        keyValueList = [element.split(":") for element in dictList]
        total = sum([int(element[1]) for element in keyValueList])
        if char in dic:
            dic[char] += total
        else:
            dic[char] = total
    for char in sorted(dic):
        dic2[char] = dic[char]
    return dic2

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """