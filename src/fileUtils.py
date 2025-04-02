import sys # Recieve command line parameters
from random import randrange as rng # Generate the data
from random import shuffle # Shuffle arrays before output to file

def fileReader(filePath: str) -> tuple:
    """
    Lee el archivo dado por argumento, con el formato igual a los archivos dados de ejemplo.\n
    PARAMETER filePath: String, indica el archivo a leer.\n
    RETURNS:   Dupla de (intervals, operations).\n
        INTERVALS:  Array de intervalos.\n
        OPERATIONS: Array de operaciones.\n
    """

    # Get file from argument
    file = open(filePath, 'r')
    firstLine = file.readline()
    elementCount = 0

    # Ignore comment if it exists
    if (len(firstLine) == 0) or (firstLine[0] == '#'):
        elementCount = int(file.readline())
    else:
        elementCount = int(firstLine)
    
    # Pre-allocating the array is slightly faster than using .append()
    intervals = [None] * elementCount
    operations = [None] * elementCount

    for i in range(elementCount):
        # Genera intervalos
        line = file.readline().split(",")

        interval = {}

        # Indispensables
        interval['ts'] = int(line[0]) # Centro del intervalo
        interval['er'] = int(line[1]) # Rango del intervalo
        interval["op"] = None  # Operacion que encaja en el intervalo
        # Para agilizar
        interval["startTime"] = int(line[0]) - int(line[1])
        interval["endTime"] = int(line[0]) + int(line[1])
        intervals[i] = interval
    for i in range(elementCount):
        # Genera operaciones
        operations[i] = int(file.readline())
    file.close()
    return intervals, operations

def dataGenerator(size: int, isRat: bool) -> tuple:
    """
    Genera intervalos y operaciones.\n
    PARAMETER size:  Integer, Cantidad de intervalos y operaciones.\n
    PARAMETER isRat: Boolean, Encaja cada operación con un intervalo o no.\n
    RETURNS:   Dupla de (intervals, operations).\n
        INTERVALS:  Array de (time stamp, error margin).\n
        OPERATIONS: Array de operation time.
    """
    intervals, operations = [None] * size, [None] * size

    for t in range(size):
        # Generates time intervals (Timestamp, Error Margin)
        interval = {}
        interval['ts'] = rng(2, 1000) # Timestamp > 1
        interval['er'] = rng(1, interval['ts']) # Timestamp > Error Margin > 0
        intervals[t] = interval # Adds created interval to list
    if isRat:
        # Generates ONE operation within each interval
        for o in range(size):
            lowerBound = intervals[o]['ts'] - intervals[o]['er']
            upperBound = intervals[o]['ts'] + intervals[o]['er']
            operations[o] = rng(lowerBound, upperBound)
    else:
        # Generates operations randomly
        for o in range(size-1):
            operations[o] = rng(1000)
    return intervals, operations

def fileCreator(isRat: bool, size: int, results: bool, outPath= "src/default_output.txt") -> str:
    """
    Genera un archivo utilizando dataGenerator().\n
    PARAMETER isRat:   Boolean, Se lo pasa a dataGenerator para saber si encajar cada operación en un intervalo o no.\n
    PARAMETER size :   Integer, Cantidad de operaciones e intervalos.\n
    PARAMETER results: Boolean, Crear o no un archivo indicando en que intervalo va cada operación.\n
    PARAMETER outPath: String, Opcional, Ruta en la cual se crea el archivo. Si existe es sobreescribido.\n
    RETURNS: String, outPath. Utilizado para pasarlo directamente a otra función.\n
    """

    intervals, operations = dataGenerator(size, isRat) # Generates the data
    
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

def main():
    """
    Si se llama directamente al archivo, ejecuta fileCreator().\n
    ARGUMENT 1: Integer. 0 Si no es la rata. 1 Si lo es. Boolean estilo C.\n
    ARGUMENT 2: Integer. Cantidad maxima de intervalos a crear.\n
    ARGUMENT 3: String. Destino a donde enviar el archivo creado.\n
    """
    
    rat = True
    if (sys.argv[1] == 0):
        rat = False

    fileCreator(rat, int(sys.argv[2]), True, outPath = sys.argv[3])

if __name__ == "__main__":
    main()