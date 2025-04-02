
# Lee el archivo dado por argumento
# Formato como ../"Archivos Test"
# Devuelve una dupla.
# Primer segmento es un array de duplas (timestamp, errorMargin)
# Segundo segmento es un array de los tiempos de operaciones
def fileReader(filePath):
    # Get file from argument
    file = open(filePath, 'r')
    firstLine = file.readline()

    elementCount = 0
    # Ignore comment if exists
    if (len(firstLine) == 0) or (firstLine[0] == '#'):
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
        timestamp["startTime"] = int(int(line[0]) - int(line[1]))
        timestamp["endTime"] = int(int(line[0]) + int(line[1]))
        timestamp["time"] = int(line[0])
        timestamp["error"] = int(line[1])
        timestamp["operation"] = None
        timestamps.append(timestamp)
    for i in range(elementCount):
        # Operations
        # (opTime)
        operations.append(int(file.readline()))
    return timestamps, operations
