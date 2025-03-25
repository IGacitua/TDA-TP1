from fileReader import *
from sorters import *

def moleFinder():
    timestamps, operations = fileReader() # Crea ambas listas
    timestampSort(timestamps) # Ordena timestamps por el margen izquierdo, como habiamos hablado. POSIBLE ZONA DE ERROR
    for i in range(len(operations)):
        operationFound = checkContains(operations[i], timestamps, i)
        if (operationFound == -1):
            # No encontró nada.
            print(f"Found false at {i} iteration.")
            return False # No es la rata
        else:
            timestamps[i] = None # Elimina de las posibilidades a esa timestamp
    return True

def checkContains(operation, timestamps, start):
    lowestFound = -1 # -1 -> nada
    for i in range(start, len(timestamps)):
        if (timestamps[i] is None):
            # Saltear si ya fue nulificada
            continue
        rangeLower = timestamps[i][0] - timestamps[i][1] # T - E
        rangeUpper = timestamps[i][0] + timestamps[i][1] # T + E
        if (operation >= rangeLower) and (operation <= rangeUpper):
            # Está dentro del rango. Inclusivo.
            if (lowestFound == -1):
                # No se encontró nada otro, sirve.
                lowestFound = i
            else:
                if (timestamps[lowestFound][1] > timestamps[i][1]):
                    # Busca cual es el que tiene menor margen de error
                    # Debería ser el mas cercano a la operación
                    # Puede ser malo?
                    lowestFound = i
                elif (timestamps[lowestFound][1] == timestamps[i][1]):
                    # Posible zona de error. No parece pero hay que agregar un criterio mas
                    print("Oh?")
    return lowestFound

if __name__ == "__main__":
    print(moleFinder())