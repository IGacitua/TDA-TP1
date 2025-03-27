from fileReader import *
from sorters import *

def moleFinder():
    timestamps, operations = fileReader() # Crea ambas listas
    appareances = createAppareanceList(timestamps, operations)
    lengthSort(appareances)
    foundTimestamps = []
    for i in range(len(appareances)):
        closest = findClosest(operations[i], appareances[i], foundTimestamps)
        if (closest == -1):
            return False
    return True

    
def createAppareanceList(timestamps, operations):
    appareances = [[]] * len(operations) 
    for o in range(len(appareances)):
        operation = operations[o]
        for t in range(len(appareances)):
            lowerBound = timestamps[t][0] - timestamps[t][1]
            upperBound = timestamps[t][0] + timestamps[t][1]
            if (operation > lowerBound) and (operation < upperBound):
                appareances[o].append(timestamps[t])
    return appareances

def findClosest(operationTime, timestamps, foundTimestamps):
    distanceSort(timestamps, operationTime)
    for i in range(len(timestamps)):
        if i not in foundTimestamps:
            foundTimestamps.append(i)
            return i
    return -1



if __name__ == "__main__":
    print(moleFinder())