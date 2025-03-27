import math
# Temp bubble sort. Reemplazar por quicksort

debug = False

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

# Ordena la lista en base a la distancia entre el centro y la operacion
def distanceSort(list, operationTime, timestamps):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (abs(timestamps[list[j]]["time"] - operationTime) > abs(timestamps[list[j+1]]["time"] - operationTime)):
                if debug:
                    print(f"{timestamps[list[j]]['time']} - {operationTime} > {timestamps[list[j+1]]['time']} - {operationTime}")
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
            elif debug:
                print(f"{timestamps[list[j]]['time']} - {operationTime} < {timestamps[list[j+1]]['time']} - {operationTime}")
        if swapped is False:
            break

# Ordena la lista en base al margen de error
def marginSort(list, operationTime, timestamps):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (timestamps[list[j]]["error"] >timestamps[list[j+1]]["error"]):
                if debug:
                    print(f"{timestamps[list[j]]['error']} > {timestamps[list[j+1]]['error']}")
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
            elif debug:
                print(f"{timestamps[list[j]]['error']} < {timestamps[list[j+1]]['error']}")
        if swapped is False:
            break

# Ordena la lista en base al borde izquierdo
def lowestSort(list, timestamps):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            lowerBoundOne = timestamps[list[j]]['time'] - timestamps[list[j]]['error']
            lowerBoundTwo = timestamps[list[j+1]]['time'] - timestamps[list[j+1]]['error']
            if (lowerBoundOne < lowerBoundTwo):
                if debug:
                    print(f"{lowerBoundOne} < {lowerBoundTwo}")
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
            elif debug:
                print(f"{lowerBoundOne} > {lowerBoundTwo}")
        if swapped is False:
            break

#Ordena la lista en base a la distancia entre el borde izquierdo y la operación
def lowestDistanceSort(list, operationTime, timestamps):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            lowerBoundOne = timestamps[list[j]]['time'] - timestamps[list[j]]['error']
            lowerBoundTwo = timestamps[list[j+1]]['time'] - timestamps[list[j+1]]['error']
            if (abs(lowerBoundOne - operationTime) > abs(lowerBoundTwo - operationTime)):
                if debug:
                    print(f"{abs(lowerBoundOne - operationTime)} > {abs(lowerBoundTwo - operationTime)}")
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
            elif debug:
                print(f"{abs(lowerBoundOne - operationTime)} < {abs(lowerBoundTwo - operationTime)}")
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

# Ordena una lista en base a la key "operations"
def operationsSort(list, timestamps):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if (timestamps[list[j]]['operations'] > timestamps[list[j+1]]['operations']):
                aux = list[j]
                list[j] = list[j+1]
                list[j+1] = aux
                swapped = True
        if swapped is False:
            break