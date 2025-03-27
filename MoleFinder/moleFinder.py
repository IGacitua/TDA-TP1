import time
from fileReader import *
from sorters import *

debug = True
startTime = time.time()


def merge_sort(arr):
    # Si la lista tiene un solo elemento o está vacía, no es necesario dividirla
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordenar ambas mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Fusionar las dos mitades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Fusionar ambas listas mientras haya elementos en ambas
    while i < len(left) and j < len(right):
        if left[i]["endTime"] > right[j]["endTime"]:  # Cambiar el signo de la comparación aquí
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

# Ejemplo de uso:


def moleFinder():
    timestamps, operations = fileReader()

    sorted_arr = merge_sort(timestamps)
    debug(sorted_arr)

def debug(timestamps):
    for t in timestamps:
        print("end: ", t["endTime"])
        


if __name__ == "__main__":
    moleFinder()





