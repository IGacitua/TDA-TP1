import time
import sys

sys.path.append('./src/') # To import from ./src
from moleFinder import *
from fileUtils import *

debug = True


def printResults(timestamps, isTheRat, testName, duration, verbose):
    print("================================")
    print("Nombre de prueba: ", testName, "")
    print("---------------")
    print("Número total de timestamps: ", len(timestamps))
    print("Tiempo total de ejecución: ", round(duration * 1000, 10), " milisegundos")
    print("---------------")
    if isTheRat:
        print("Resultado: Es la rata!")
    else:
        print("Resultado: NO es la rata!")

    if verbose and len(timestamps) > 0:
        print("---------------")
        print("Asignaciones: \n")
        for timestamp in timestamps:
            print(
                timestamp["op"],
                " --> ",
                timestamp["ts"],
                " ± ",
                timestamp["er"]
            )
    print("\n")


if __name__ == "__main__":
    verbose = True     # Especifica si se quiere imprimir en la salida todas las asignaciones


    testFilePaths = sys.argv[1:]
    print(testFilePaths)

    for testFilePath in testFilePaths:
        timestamps, operations = fileReader(testFilePath)
        filePathSplitted = testFilePath.split("/")
        testName = filePathSplitted[len(filePathSplitted) - 1]

        result_array = []

        start_time = time.time()
        result = moleFinder(timestamps, operations, result_array)
        totalTime = time.time() - start_time

        printResults(result_array, result, testName, totalTime, verbose)

