import time
debug = True
startTime = time.time()
import sys

sys.path.append('./src/')
from moleFinder import *
from fileReader import *

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
        timestamps, operations = fileReader("tests/" + testName)

        result_array = []

        start_time = time.time()
        result = moleFinder(timestamps, operations, result_array)
        totalTime = time.time() - start_time

        printResults(result_array, result, testName, totalTime, verbose)

