import time
from moleFinder import moleFinder
from fileReader import fileReader
from intervalGenerator import fileCreator
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

debug = False

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

# Funcion que utiliza curve_fit para aproximar tiempos
def f(x, c1, c2):
    return c1 * x + c2

def plotTime(x_values, precision, generatorSteps):
    y_values = []
    for i in x_values:
        timestamps, operations = fileReader(fileCreator(True, i))
        y_values.append(averageTime(moleFinder, precision, timestamps, operations, []))
    c, pcov = curve_fit(f, x_values, y_values)
    if debug:
        print(f"X: {x_values}")
        print(f"Y: {y_values}")
        print(f"C: {c}")

    xInterval = generatorSteps * (len(x_values) // 10) # Interval at which the X axis has markers

    plt.plot(x_values, y_values, label = "Original", c = "Black", linestyle="solid", marker=".", alpha = 0.5)
    plt.plot(x_values, [c[0] * n + c[1] for n in x_values], label = "Adjusted", c = "Red", linestyle="dotted")
    plt.xlabel("Interval count")
    plt.ylabel("Execution Time (ms)")
    plt.xticks(range(0, x_values[-1], xInterval)) 
    plt.legend()
    plt.show()


if __name__ == '__main__':
    steps = 10
    interval = [i for i in range(0,1000, steps)]
    precision = 25

    plotTime(interval, precision, steps)
    pause = input()