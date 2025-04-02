import sys
import random

def intervalGenerator(size, isRat, setSeed, seed):
    intervals = []
    operations = []
    if setSeed:
        random.seed(seed)
    for i in range(size):
        interval = {}
        timeStamp   = random.randrange(2, 1000) # Timestamp > 1
        errorMargin = random.randrange(1, timeStamp) # Timestamp > Error Margin > 0
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

def fileCreator(isRat, size, results, setSeed = False, seed = 0, outPath = "src/default_output.txt"):
    intervals, operations = intervalGenerator(size, isRat, setSeed, seed)
    mainFile = open(outPath, 'w')
    mainFile.write(f"# File generated automatically. Size {size}. Rat = {isRat}\n")
    mainFile.write(f"{str(size)}\n")
    if (isRat and results):
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
    return outPath

if __name__ == "__main__":
    # Input:
    # python intervalGenerator.py INT SIZE PATH
    # Int -> 0 si no rata, 1 si rata
    # Size -> Numero de intervalos
    # Path -> Nombre del archivo out
    rat = True
    if (sys.argv[1] == 0):
        rat = False
    fileCreator(rat, int(sys.argv[2]), True, outPath = sys.argv[3])