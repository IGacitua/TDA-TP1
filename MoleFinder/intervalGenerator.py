import sys
import random

def intervalGenerator(size, isRat):
    intervals = []
    operations = []
    for i in range(size):
        interval = {}
        timeStamp   = random.randrange(1000)
        errorMargin = random.randrange(5, timeStamp)
        interval['ts'] = timeStamp
        interval['er'] = errorMargin
        intervals.append(interval)
    if isRat:
        for o in range(size):
            lowerBound = intervals[o]['ts'] - intervals[o]['er']
            upperBound = intervals[o]['ts'] + intervals[o]['er']
            operations.append(random.randrange(lowerBound, upperBound))
    else:
        for o in range(size-1):
            operations.append(random.randrange(1000))
    return intervals, operations

def fileCreator(outPath, size, isRat):
    intervals, operations = intervalGenerator(size, isRat)
    mainFile = open(outPath, 'w')
    mainFile.write(f"# File generated automatically. Size {size}. Rat = {isRat}\n")
    mainFile.write(f"{str(size)}\n")
    if (isRat):
        subFile = open(outPath + ' - RESULTS', 'w')
        for i in range(size):
            line = f"{operations[i]} --> {intervals[i]['ts']} +/- {intervals[i]['er']} \n"
            subFile.write(line)
    random.shuffle(intervals)
    random.shuffle(operations)
    for i in range(size):
        mainFile.write(f"{intervals[i]['ts']},{intervals[i]['er']}\n")
    for i in range(size):
        mainFile.write(f"{operations[i]}\n")

if __name__ == "__main__":
    # Input:
    # python intervalGenerator.py INT SIZE PATH
    # Int -> 0 si no rata, 1 si rata
    # Size -> Numero de intervalos
    # Path -> Nombre del archivo out
    rat = True
    if (sys.argv[1] == 0):
        rat = False
    fileCreator(sys.argv[3], int(sys.argv[2]), rat)