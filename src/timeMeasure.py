# Python libraries
from os import remove as deleteFile
from sys import maxsize
from random import randrange as rng
from time import time as currentTime
from math import log
# External libraries
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
# Internal libraries
from moleFinder import moleFinder as measurableFunction # AS para poder reutilizar el codigo
from intervalGenerator import fileCreator
from fileReader import fileReader

debug = True

# Return digit count of number
def digits(num):
    return len(str(num))

# Ejecuta FUNCTION con PARAMS, devuelve el tiempo de ejecución
def measureTime(function, *params):
    startTime = currentTime() # Current time
    function(*params) # Executes function
    return currentTime() - startTime # Returns elapsed time

# Mide el tiempo de ejecución de FUNCTION con PARAMS, PRECISION veces y devuelve el promedio
def averageTime(function, precision, *params):
    sum = 0 # Suma de todos los tiempos
    for i in range(precision):
        sum += measureTime(function, *params)
    return sum / precision # Suma / Cantidad = Promedio

# Funcion cuadrática
def quadratic(x, c1, c2, c3):
    return c1 * (x**2) + c2 * x + c3

# Obtiene el tiempo de ejecución promedio de FUNC con X_VALUES, con un promedio obtenido de PRECISION iteraciones
# Plotea la función original, y su curve_fit utilizando F
# GENERATORSTEPS es cada cuanto varía cada valor de X (0,10,20,30,40,50) tiene STEPS de 10. Se utiliza para los ejes.
def plotTime(x_values, precision, generatorSteps, f):
    y_values_original = [] # Variables dependientes de la función sin ajustar

    width = digits(x_values[-1]) # Usado exclusivamente para prints
    file = '' # Creo la variable fuera del loop para solo tener que borrar una vez el archivo
    for i in range(len(x_values)):
        file = fileCreator(True, x_values[i], False) # Al usar siempre el mismo archivo no necesito setear semilla
        timestamps, operations = fileReader(file) # Obtiene los parametros utilizados por moleReader
        # NOTA: De reutilizar la función, cambiar linea de arriba
        y_values_original.append(averageTime(measurableFunction, precision, timestamps, operations, []))
        if debug:
            print(f"{x_values[i]:>0{width}}: {y_values_original[-1]:.5f}s")
    deleteFile(file) # Borra el archivo luego de uso. El loop sobreescribe asi que esto puede estar fuera

    c, pcov = curve_fit(f, x_values, y_values_original) # Obtiene la variación de X/Y en base a F
    y_values_adjusted = [f(n,c[0],c[1], c[2]) for n in x_values] # Obtiene los valores ajustados en base a variación

    if debug:
        print(f"X: {x_values}")
        print(f"Y: {y_values_original}")
        print(f"C: {c}")

    # PLOT
    plt.plot(x_values, y_values_original, label = "Original", c = "Black", linestyle="solid", marker='.', alpha = 0.75) # Plot original
    plt.plot(x_values, y_values_adjusted, label = f.__name__.title(), c = "Red", linestyle="dashed") # Plot ajustada

    # LABELS
    plt.xlabel("Interval count")
    plt.ylabel("Execution Time (s)")
    plt.title(f"Execution times for {len(x_values) - 1} intervals.", loc = 'left')
    xInterval = generatorSteps * (len(x_values) // 10) # Intervalo en el cual el eje X tiene marcadores
    plt.xticks(range(0, x_values[-1] + xInterval, xInterval)) # Aplico lo de la linea de arriba
    plt.show() # Muestro el gráfico


if __name__ == '__main__':
    steps = 100
    precision = 50
    intervalCount = 10000
    interval = [i for i in range(0,intervalCount + 1, steps)]

    plotTime(interval, precision, steps, quadratic)