from sorting import sortIntervalsByEnd as sortIntervals

def moleFinder(intervals: list, operations: list, result_array: list = None):
    """
    Función Principal.\n
    Dado intervalos y operaciones, indica si cada operación tiene un intervalo en el que encaja.\n
    Un intervalo no puede contener multiples operaciones.\n
    PARAMETER intervals:    Lista de Diccionarios, dado por fileReader().\n
    PARAMETER operations:   Lista de Integers, dado por fileReader().\n
    PARAMETER result_array: Lista vacía, Opcional. Se guarda en que intervalo encaja cada operación.\n
    RETURNS: Boolean. Si se pudieron encajar todas las operaciones con un intervalo o no.\n
    """
    sortedIntervals = sortIntervals(intervals)

    for operation in operations:
        timestampFound = False
        for timestamp in sortedIntervals:
            if operation >= timestamp["startTime"] and operation <= timestamp["endTime"] and timestamp["op"] is None:
                timestampFound = True
                timestamp["op"] = operation
                result_array.append(timestamp)
                break
        if not timestampFound:
            # Ningun timestamp contenia a la operacion. No es la rata
            return False
    return True
