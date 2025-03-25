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
        line = file.readline().split(",")
        timestamps.append((int(line[0]), int(line[1].strip('\n'))))
    for i in range(elementCount):
        operations.append(int(file.readline()))
    return timestamps, operations
