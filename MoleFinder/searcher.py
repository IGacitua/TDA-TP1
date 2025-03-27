def searchLowest(operations, timestamps):
    currentLowest = 0
    lowestLength = None
    for i in range(len(operations)):
        currentLength = intervalCount(operations[i]["intervals"], timestamps)
        if i == 0:
            lowestLength = currentLength
        else:
           if currentLength < lowestLength:
                lowestLength = currentLength
                currentLowest = i
    return currentLowest

def intervalCount(operation, timestamps):
    ret = 0
    for i in range(len(operation)):
        if (timestamps[operation[i]]["found"] is False):
            ret += 1
    return ret