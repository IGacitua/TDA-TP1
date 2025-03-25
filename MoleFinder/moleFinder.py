from fileReader import *
from sorters import *

def moleFinder():
    timestamps, operations = fileReader()
    timestampSort(timestamps)
    for i in range(len(operations)):
        operationFound = checkContains(operations[i], timestamps, i)
        if (operationFound == -1):
            print(f"Found false at {i} iteration.")
            return False
        else:
            timestamps[i] = None
    return True

def checkContains(operation, timestamps, start):
    lowestFound = -1
    for i in range(start, len(timestamps)):
        if (timestamps[i] is None):
            continue
        rangeLower = timestamps[i][0] - timestamps[i][1]
        rangeUpper = timestamps[i][0] + timestamps[i][1]
        if (operation >= rangeLower) and (operation <= rangeUpper):
            if (lowestFound == -1):
                lowestFound = i
            else:
                if (timestamps[lowestFound][1] > timestamps[i][1]):
                    lowestFound = i
    return lowestFound

if __name__ == "__main__":
    print(moleFinder())