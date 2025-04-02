def sortIntervalsByEnd(arr):
    """
    Ordena el array de intervalos en base a su tiempo de fin, mediante Merge Sort.\n
    PARAMETER arr: Array a ordenar.\n
    RETURNS: El array ordenado. El arreglo original queda intacto.\n
    """

    # Si la lista tiene un solo elemento o está vacía,
    # no es necesario dividirla
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordenar ambas mitades
    left_half = sortIntervalsByEnd(left_half)
    right_half = sortIntervalsByEnd(right_half)

    # Fusionar las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    """
    Función utilizada por merge sort.\n
    """
    sorted_arr = []
    i = j = 0

    # Fusionar ambas listas mientras haya elementos en ambas
    while i < len(left) and j < len(right):
        if left[i]["endTime"] < right[j]["endTime"]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Si quedan elementos en 'left', agregarlos
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    # Si quedan elementos en 'right', agregarlos
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr
