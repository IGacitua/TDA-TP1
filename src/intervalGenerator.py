import sys # Recieve command line parameters
from random import randrange as rng # Generate the data
from random import shuffle # Shuffle arrays before output to file

# Creates intervals and operations
# If isRat, matches each operation with an interval
def intervalGenerator(size, isRat):
    intervals, operations = [], []
    for i in range(size):
        # Generates time intervals (Timestamp, Error Margin)
        interval = {}
        interval['ts'] = rng(2, 1000) # Timestamp > 1
        interval['er'] = rng(1, interval['ts']) # Timestamp > Error Margin > 0
        intervals.append(interval) # Adds created interval to list
    if isRat:
        # Generates ONE operation within each interval
        for o in range(size):
            lowerBound = intervals[o]['ts'] - intervals[o]['er']
            upperBound = intervals[o]['ts'] + intervals[o]['er']
            operations.append(rng(lowerBound, upperBound))
    else:
        # Generates operations randomly
        for o in range(size-1):
            operations.append(rng(1000))
    return intervals, operations

# Creates a file with the contents from intervalGenerator()
# outPath is optional
def fileCreator(isRat, size, results, outPath = "src/default_output.txt"):
    intervals, operations = intervalGenerator(size, isRat) # Generates the data
    mainFile = open(outPath, 'w') 
    mainFile.write(f"# File generated automatically. Size {size}. Rat = {isRat}\n") # First line is a comment
    mainFile.write(f"{str(size)}\n") # Second line is the interval/operation count

    # Crea un archivo diciendo en cual intervalo va cada operación
    if (isRat and results):
        subFile = open(outPath + ' - RESULTS', 'w')
        for i in range(size):
            line = f"{operations[i]} --> {intervals[i]['ts']} +/- {intervals[i]['er']} \n"
            subFile.write(line)

    # Desordena ambas listas
    shuffle(intervals)
    shuffle(operations)

    # Crea el resto archivo principal
    for i in range(size):
        mainFile.write(f"{intervals[i]['ts']},{intervals[i]['er']}\n")
    for i in range(size):
        mainFile.write(f"{operations[i]}\n")
    
    return outPath # Devuelve donde es guarda el archivo final, para poder mandar directamente a otra función

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