from fileReader import *
from sorters import *

def moleFinder():
    timestamps, operations = fileReader()
    timestampSort(timestamps)
    for i in range(len(operations)):
        operationFound = checkContains(operations[i], timestamps, i)
        if (operationFound == -1):
            return False
        else:
            timestamps[i] = None
    return True

def checkContains(operation, timestamps, start):
    contentArray = []
    for i in range(start, len(timestamps)):
        if (timestamps[i] is None):
            continue
        rangeLower = timestamps[i][0] - timestamps[i][1]
        rangeUpper = timestamps[i][0] + timestamps[i][1]
        if (operation > rangeLower) and (operation < rangeUpper):
            contentArray.append(i)
    marginSort(contentArray)
    if (len(contentArray) == 0):
        return -1
    else:
        return contentArray[0]
    

if __name__ == "__main__":
    print(moleFinder())