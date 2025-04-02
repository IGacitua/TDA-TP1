# Python libraries
from os import remove as deleteFile # Delete excess files
from sys import argv # Recieve command line parameters
from time import time as currentTime # Measure time
from datetime import datetime # To name files with current hour
# External libraries
from matplotlib import pyplot as plt # Graphics
from scipy.optimize import curve_fit # Adjust data to function
# Internal libraries
from moleFinder import moleFinder as measurableFunction # AS para poder reutilizar el codigo
from intervalGenerator import fileCreator # Generates disposable data
from fileReader import fileReader # Reads the generated data

debug = True

# Return digit count of number
def digits(num):
    return len(str(num))

# Ejecuta FUNCTION con PARAMS, devuelve el tiempo de ejecución en milisegundo
def measureTime(function, *params):
    startTime = currentTime() # Current time
    function(*params) # Executes function
    return (currentTime() - startTime) * 1000 # Returns elapsed time

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
    p_id = datetime.now().microsecond # ID so you can run the program multiple times in paralel
    y_values_original = [] # Variables dependientes de la función sin ajustar

    width = digits(x_values[-1]) # Usado exclusivamente para prints
    for i in range(len(x_values)):
        dt = f"{datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}"
        # Nombro el archivo para poder ejecutar dos instancias del programa sin problema
        file = fileCreator(True, x_values[i], False, outPath=f"Automatic {p_id}-{dt}.txt") # Al usar siempre el mismo archivo no necesito setear semilla
        timestamps, operations = fileReader(file) # Obtiene los parametros utilizados por moleReader
        # NOTA: De reutilizar la función, cambiar linea de arriba
        y_values_original.append(averageTime(measurableFunction, precision, timestamps, operations, []))
        if debug:
            print(f"{x_values[i]:>0{width}}: {y_values_original[-1]:.2f}ms") # Ej: 02900: 45.97ms
        deleteFile(file) # Borra el archivo luego de uso.

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
    plt.ylabel("Execution Time (ms)")
    plt.title(f"Average times for {len(x_values) - 1} executions.", loc = 'left')
    
    # X/Y axis marks.
    highestX = x_values[-1]
    highestY = max(y_values_original[-1], y_values_adjusted[-1])
    xTicks, yTicks = [],[]
    for i in range(11):
        xTicks.append(round((highestX / 10) * i, 2))
        yTicks.append(round((highestY / 10) * i, 2))
    plt.xticks(xTicks)
    plt.yticks(yTicks)

    plt.legend()
    plt.show() # Muestro el gráfico


if __name__ == '__main__':
    # ARGUMENT 1: Steps
    # ARGUMENT 2: Precision
    # ARGUMENT 3: Maximum Intervals
    print(f"Running {int(argv[3]) // int(argv[1])} iterations with {argv[2]} precision.")
    interval = [i for i in range(0, int(argv[3]) + 1, int(argv[1]))]

    plotTime(interval, int(argv[2]), int(argv[1]), quadratic)