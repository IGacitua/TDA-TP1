import math
# Temp bubble sort. Reemplazar por quicksort

debug = True

# Ordena la lista en función de borde izquierdo
# DEPRECATED
def timestampSort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            differenceOne = list[j][0] - list[j][1]
            differenceTwo = list[j+1][0] - list[j+1][1]
            if (differenceOne > differenceTwo):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
        if swapped is False:
            break

# Ordena la lista en función del margen de error
# DEPRECATED
def marginSort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (list[j][1] > list[j+1][1]):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
        if swapped is False:
            break

# Ordena la lista en función del centro del intervalo
# DEPRECATED
def centerSort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (list[j][0] > list[j+1][0]):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
        if swapped is False:
            break

#Ordena la lista en función de la distancia entre el centro del intervalo y la operación
def distanceSort(list, operationTime):
    for i in range(len(list)):
        if (debug is True):
            print(f"Sort Nº{i}")
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (abs(operationTime - list[j][0]) > abs(operationTime - list[j+1][0])):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
        if swapped is False:
            break

# Ordena una lista de listas en base a la longitud de la lista
def lengthSort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (len(list[j]) > len(list[j+1])):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
        if swapped is False:
            break