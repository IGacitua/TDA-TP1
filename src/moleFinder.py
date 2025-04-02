from sorters import sort_timestamps_by_end_time

def moleFinder(timestamps, operations, result_array):
    sorted_timestamps = sort_timestamps_by_end_time(timestamps)

    for operation in operations:
        timestampContainingOperationThatEndsSooner = None
        for timestamp in sorted_timestamps:
            if operation >= timestamp["startTime"] and operation <= timestamp["endTime"] and timestamp["operation"] is None:
                if timestampContainingOperationThatEndsSooner is None or timestamp["endTime"] < timestampContainingOperationThatEndsSooner["endTime"]:
                    # Se guarda el timestamp que contiene la operacion, termina antes y no tenia ninguna operación asignada
                    timestampContainingOperationThatEndsSooner = timestamp
        if timestampContainingOperationThatEndsSooner is None:
            # Ningun timestamp contenia a la operacion. No es la rata
            return False
        else:
            timestampContainingOperationThatEndsSooner["operation"] = operation

    isTheRat = True
    for timestamp in sorted_timestamps:
        result_array.append(timestamp)
        if timestamp["operation"] is None:
            isTheRat = False
    
    return isTheRat
