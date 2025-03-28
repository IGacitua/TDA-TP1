import time
from fileReader import *
from sorters import *
import sys

debug = True
startTime = time.time()


def merge_sort(arr):
    # Si la lista tiene un solo elemento o está vacía, no es necesario dividirla
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordenar ambas mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Fusionar las dos mitades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Fusionar ambas listas mientras haya elementos en ambas
    while i < len(left) and j < len(right):
        if left[i]["endTime"] < right[j]["endTime"]:  # Cambiar el signo de la comparación aquí
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Si quedan elementos en 'left', agregarlos
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    # Si quedan elementos en 'right', agregarlos
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr

# Ejemplo de uso:


def moleFinder(timestamps, operations, result_array):
    sorted_timestamps = merge_sort(timestamps)

    for operation in operations:
        timestampContainingOperationThatEndsSooner = None
        for timestamp in sorted_timestamps:
            if operation >= timestamp["startTime"] and operation <= timestamp["endTime"] and timestamp["operation"] is None:
                if timestampContainingOperationThatEndsSooner is None or timestamp["endTime"] < timestampContainingOperationThatEndsSooner["endTime"]:
                    # Se guarda el timestamp que contiene la operacion, termina antes y no tenia ninguna operación asignada
                    timestampContainingOperationThatEndsSooner = timestamp
        if timestampContainingOperationThatEndsSooner is None:
            # Ningun timestamp contenia a la operacion. No es la rata
            return False
        else:
            timestampContainingOperationThatEndsSooner["operation"] = operation

    isTheRat = True
    for timestamp in sorted_timestamps:
        result_array.append(timestamp)
        if timestamp["operation"] is None:
            isTheRat = False
    
    return isTheRat


def printResults(timestamps, isTheRat, testName, duration, verbose):
    print("================================")
    print("Nombre de prueba: ", testName, "")
    print("---------------")
    print("Número total de timestamps: ", len(timestamps))
    print("Tiempo total de ejecución: ", round(duration * 1000, 10), " milisegundos")
    print("---------------")
    if isTheRat:
        print("Resultado: Es la rata!!!")
    else:
        print("Resultado: NO es la rata!!!")

    if verbose and len(timestamps) > 0:
        print("---------------")
        print("Asignaciones: \n")
        for timestamp in timestamps:
            print(
                timestamp["operation"],
                " --> ",
                timestamp["time"],
                " ± ",
                timestamp["error"]
            )
    print("\n")


if __name__ == "__main__":
    verbose = True     # Especifica si se quiere imprimir en la salida todas las asignaciones

    testNames = [
        "5-es.txt",
        "5-no-es.txt",
        "10-es.txt",
        "10-es-bis.txt",
        "10-no-es.txt",
        "10-no-es-bis.txt",
        "50-es.txt",
        "50-no-es.txt",
        "100-es.txt",
        "100-no-es.txt",
        "500-es.txt",
        "500-no-es.txt",
        "1000-es.txt",
        "1000-no-es.txt",
        "5000-es.txt",
        "5000-no-es.txt"
    ]

    for testName in testNames:
        timestamps, operations = fileReader("Tests/" + testName)

        result_array = []

        start_time = time.time()
        result = moleFinder(timestamps, operations, result_array)
        totalTime = time.time() - start_time

        printResults(result_array, result, testName, totalTime, verbose)
    






