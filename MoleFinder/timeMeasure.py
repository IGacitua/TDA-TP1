from matplotlib import pyplot as plt
from moleFinder import *
from fileReader import *
from intervalGenerator import *
from scipy.optimize import curve_fit
import time

# Ejecuta FUNCTION con PARAMS, devuelve el tiempo de ejecución
def measureTime(function, *params):
    startTime = time.time()
    function(*params)
    return time.time() - startTime

# Mide el tiempo de ejecución de FUNCTION con PARAMS, PRECISION veces y devuelve el promedio
def averageTime(function, precision, *params):
    sum = 0
    for i in range(precision):
        sum += measureTime(function, *params)
    return sum / precision

# Genera promedios para archivos con LENGTH intervalos
def dataGenerator(length):
    timestamps, operations = fileReader(fileCreator(True, length))
    average = averageTime(moleFinder, 10, timestamps, operations, [])
    print(f"Average for length {length}: {average}")
    return average

# Funcion que utiliza curve_fit para aproximar tiempos
def f(x, c1, c2):
    return c1 * x + c2

def plotTime(x_values):
    y_values = []
    for i in x_values:
        y_values.append(dataGenerator(i))
    c, pcov = curve_fit(f, x_values, y_values)
    print(f"X: {x_values}")
    print(f"Y: {y_values}")
    print(f"C: {c}")
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label = "Original")
    ax.plot(x_values, [c[0] * n + c[1] for n in x_values], 'r--', label="Ajuste")
    ax.legend()
    plt.show()

plotTime([10,20,30,40,50])
pause = input()