import time
import os
from moleFinder import moleFinder
from fileReader import fileReader
from intervalGenerator import fileCreator
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

debug = True

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

# Funcion lineal
def lineal(x, c1, c2):
    return c1 * x + c2

# Funcion cuadrática
def cuadratic(x, c1, c2, c3):
    return c1 * (x**2) + c2 * x + c3

# Obtiene el tiempo de ejecución promedio de moleFinder con X_VALUES, con un promedio obtenido de PRECISION iteraciones
# Plotea la función original, y su curve_fit utilizando F
# GENERATORSTEPS es cada cuanto varía cada valor de X (0,10,20,30,40,50) tiene STEPS de 10. Se utiliza para los ejes.
def plotTime(x_values, precision, generatorSteps, f):
    y_values_original = []
    for i in range(len(x_values)):
        file = fileCreator(True, x_values[i], False)
        timestamps, operations = fileReader(file)
        os.remove(file) 
        y_values_original.append(averageTime(moleFinder, precision, timestamps, operations, []))
        print(f"{x_values[i]}: {y_values_original[-1]}")
    c, pcov = curve_fit(f, x_values, y_values_original)
    y_values_adjusted = [f(n,c[0],c[1], c[2]) for n in x_values]
    if debug:
        print(f"X: {x_values}")
        print(f"Y: {y_values_original}")
        print(f"C: {c}")

    xInterval = generatorSteps * (len(x_values) // 10) # Interval at which the X axis has markers

    plt.plot(x_values, y_values_original, label = "Original", c = "Black", linestyle="solid", marker=".", alpha = 0.5)
    plt.plot(x_values, y_values_adjusted, label = f.__name__.title(), c = "Red", linestyle="dotted")
    plt.xlabel("Interval count")
    plt.ylabel("Execution Time (ms)")
    plt.xticks(range(0, x_values[-1] + xInterval, xInterval)) 
    plt.legend()
    plt.show()


if __name__ == '__main__':
    steps = 50
    precision = 10
    interval = [i for i in range(0,1000, steps)]

    plotTime(interval, precision, steps, cuadratic)