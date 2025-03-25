# Temp bubble sort. Reemplazar por quicksort


# Ordena el array en función de borde izquierdo
def timestampSort(timestamps):
    for i in range(len(timestamps)):
        swapped = False
        for j in range(0, len(timestamps) - i - 1):
            differenceOne = timestamps[j][0] - timestamps[j][1]
            differenceTwo = timestamps[j+1][0] - timestamps[j+1][1]
            if (differenceOne > differenceTwo):
                aux = timestamps[j]
                timestamps[j] = timestamps[j+1]
                timestamps[j+1] = aux
                swapped = True
        if swapped is False:
            break

# Ordena el array en función del margen de error
def marginSort(timestamps):
    for i in range(len(timestamps)):
        swapped = False
        for j in range(0, len(timestamps) - i - 1):
            if (timestamps[j][1] > timestamps[j+1][1]):
                aux = timestamps[j]
                timestamps[j] = timestamps[j+1]
                timestamps[j+1] = aux
                swapped = True
        if swapped is False:
            break