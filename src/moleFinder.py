from timestampSort import sortIntervalsByEnd as sortIntervals

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
        intervalContainingOperationThatEndsSooner = None
        for interval in sortedIntervals:
            if (operation >= interval["startTime"]) and (operation <= interval["endTime"]) and (interval["op"] is None):
                if intervalContainingOperationThatEndsSooner is None or interval["endTime"] < intervalContainingOperationThatEndsSooner["endTime"]:
                    # Se guarda el timestamp que contiene la operacion, termina antes y no tenia ninguna operación asignada
                    intervalContainingOperationThatEndsSooner = interval
        if intervalContainingOperationThatEndsSooner is None:
            # Ningun timestamp contenia a la operacion. No es la rata
            return False
        else:
            intervalContainingOperationThatEndsSooner["op"] = operation
            if (result_array is not None):
                result_array.append(intervalContainingOperationThatEndsSooner)
    return True
