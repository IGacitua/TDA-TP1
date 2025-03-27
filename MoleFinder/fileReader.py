import sys

# Lee el archivo dado por argumento
# Formato como ../"Archivos Test"
# Devuelve una dupla.
# Primer segmento es un array de duplas (timestamp, errorMargin)
# Segundo segmento es un array de los tiempos de operaciones
def fileReader():
    # Get file from argument
    filePath = sys.argv[1]
    file = open(filePath, 'r')
    firstLine = file.readline()

    elementCount = 0
    # Ignore comment if exists
    if (firstLine[0] == '#'):
        elementCount = int(file.readline())
    else:
        elementCount = int(firstLine)
    
    timestamps = []
    operations = []
    for i in range(elementCount):
        # Timestamps
        # {time, error, found}
        timestamp = {}
        line = file.readline().split(",")
        timestamp["time"] = int(line[0])
        timestamp["error"] = int(line[1].strip('\n'))
        timestamp["found"] = False
        timestamp["operations"] = 0 # En cuantas operaciones aparece la timestamp
        timestamps.append(timestamp)
    for i in range(elementCount):
        # Operations
        # (opTime)
        operations.append(int(file.readline()))
    return timestamps, operations
