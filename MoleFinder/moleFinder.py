from fileReader import *
from sorters import *
import time # For testing

debug = True
startTime = time.time()

def moleFinder():

    timestamps, operations = fileReader() # Crea ambas listas
    if (debug is True):
        print(timestamps)
        print(operations)
    appareances = createAppareanceList(timestamps, operations)
    print(appareances)
    lengthSort(appareances)
    print(appareances)
    foundTimestamps = []
    i = 0
    for i in range(len(appareances)):
        #if (debug is True):
            #print(f"Iteration {i}, {(time.time() - startTime):.2f}s since start.")
        closest = findClosest(operations[i], appareances[i], foundTimestamps)
        if (closest == -1):
            return False
    if (debug is True):
        print(f"Operation {i}, time {operations[i]}")
        centerSort(foundTimestamps)
        print(f"Timestamps: {foundTimestamps}")    
    return True

    
def createAppareanceList(timestamps, operations):
    appareances = [[] for Null in range(len(operations))]
    for o in range(len(appareances)):
        #if (debug is True):
            #print(f"Operation {o}, {(time.time() - startTime):.2f}s since start.")
        operation = operations[o]
        for t in range(len(appareances)):
            lowerBound = timestamps[t][0] - timestamps[t][1]
            upperBound = timestamps[t][0] + timestamps[t][1]
            if (operation >= lowerBound) and (operation <= upperBound):
                (appareances[o]).append(timestamps[t])
        print(f"Operation {operations[o]}: {appareances[o]} ")
    #print(appareances)
    return appareances

def findClosest(operationTime, timestamps, foundTimestamps):
    distanceSort(timestamps, operationTime)
    print(timestamps)
    #marginSort(timestamps)
    for i in range(len(timestamps)):
        #if (debug is True):
            #print(f"Timestamp {i}: {timestamps[i]}")
        if timestamps[i] not in foundTimestamps:
            foundTimestamps.append(timestamps[i])
            if (debug is True):
                print(f"{operationTime} -> {timestamps[i][0]} ± {timestamps[i][1]}")
            return i
    return -1



if __name__ == "__main__":
    print(moleFinder())
    print(f"{(time.time() - startTime):.2f}s since start.")