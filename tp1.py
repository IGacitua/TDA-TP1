import time
import sys

sys.path.append('./src/') # To import from ./src
from moleFinder import *
from fileUtils import *

def printResults(intervals: list, isRat: bool, testName: str, duration: float, verbose: bool):
    print("================================")
    print("Nombre de prueba: ", testName, "")
    print("---------------")
    print("Número total de intervalos: ", len(intervals))
    print("Tiempo total de ejecución: ", round(duration * 1000, 10), " milisegundos")
    print("---------------")
    if isRat:
        print("Resultado: Es la rata!")
    else:
        print("Resultado: No es la rata!")

    if verbose and len(intervals) > 0:
        print("---------------")
        print("Asignaciones: \n")
        for timestamp in intervals:
            print(
                timestamp["op"],
                " --> ",
                timestamp["ts"],
                " ± ",
                timestamp["er"]
            )
    print("\n")

def main():
    """
    Ejecuta moleFinder() e imprime resultados.\n
    """
    verbose = False # Especifica si se quiere imprimir en la salida todas las asignaciones

    testFilePaths = sys.argv[1:]
    print(testFilePaths)

    for testFilePath in testFilePaths:
        intervals, operations = fileReader(testFilePath)
        filePathSplitted = testFilePath.split("/")
        testName = filePathSplitted[len(filePathSplitted) - 1]

        result_array = []

        start_time = time.time()
        result = moleFinder(intervals, operations, result_array)
        totalTime = time.time() - start_time

        printResults(result_array, result, testName, totalTime, verbose)

if __name__ == "__main__":
    main()