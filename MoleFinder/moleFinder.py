import time
from fileReader import *
from sorters import *

debug = True
startTime = time.time()

def moleFinder():
    timestamps, operations = fileReader() # Crea ambas listas
    appareances = createAppareanceList(timestamps, operations)
    if (debug):
        print(timestamps)
    #    print(operations)
    #    print(appareances)
    lengthSort(appareances)
    i = 0
    for i in range(len(appareances)):
        if debug:
            print(f"\nOperation {appareances[i]['opTime']}")
        closest = findClosest(appareances[i], timestamps)
        if (closest == -1):
            if debug:
                print(f"Operation {appareances[i]['opTime']} has no interval.")
            return False # No mole
        else:
            timestamps[closest]["found"] = True
    return True


def createAppareanceList(timestamps, operations):
    appareances = [{} for Null in range(len(operations))]

    # len(operations) == len(timestamps) == len(appareances) si no hay errores.
    for op in range(len(operations)):
        operation = operations[op]
        appareances[op]["opTime"] = operation
        appareances[op]["intervals"] = []
        for ts in range(len(timestamps)):
            lowerBound = timestamps[ts]["time"] - timestamps[ts]["error"]
            upperBound = timestamps[ts]["time"] + timestamps[ts]["error"]
            if (operation >= lowerBound) and (operation <= upperBound):
                appareances[op]["intervals"].append(ts) # Guardo el indice de la timestamp, en relacion a la lista completa.
                timestamps[ts]["operations"] += 1
        if (debug):
            print(f"Operation {operations[op]}, {(time.time() - startTime):.4f}s since start, intervals:", end=" ")
            printTimestamps(appareances[op]["intervals"], timestamps)
    return appareances

def findClosest(operation, timestamps):
    opTime = operation["opTime"]
    lowestDistanceSort(operation["intervals"], opTime, timestamps) # Quizá innecesario. Quizá haga que deje de ser O(n^2)
    if (debug):
        printTimestamps(operation['intervals'], timestamps)
    for ts in operation["intervals"]:
        if (timestamps[ts]["found"] is False):
            print(f"{opTime} -> {timestamps[ts]['time']} ± {timestamps[ts]['error']}")
            return ts
    return -1

# Funcion debug
def printTimestamps(appareances, timestamps):
    iteration = 0
    for i in appareances:
        if iteration < len(appareances)-1:
            print(f"{timestamps[i]['time']}", end=', ')
        else:
            print(f"{timestamps[i]['time']}", end='.\n')
        iteration += 1


if __name__ == "__main__":
    print(moleFinder())
    print(f"{(time.time() - startTime):.4f}s since start.")