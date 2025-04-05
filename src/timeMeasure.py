# Python libraries
from sys import argv # Recieve command line parameters
from time import time as currentTime # Measure time
from collections.abc import Callable # Type Hint -> Function
from datetime import datetime # To name files with current hour
from copy import deepcopy # To copy data
# External libraries
from matplotlib import pyplot as plt # Graphics
from numpy import max as arrayMaximum # Get highest element of array
from scipy.optimize import curve_fit # Adjust data to function
# Internal libraries
from moleFinder import moleFinder as measurableFunction # AS para poder reutilizar el codigo
from fileUtils import dataSimulator as simulationFunction # Generates disposable data

debug = True

def digits(num: any) -> int:
    """
    Devuelve cantidad de digitos de num.\n
    """
    return len(str(num))

def measureTime(f: Callable, *params) -> float:
    """
    Mide el tiempo de ejecución de la función.\n
    PARAMETER f: Function, La función a medir.\n
    PARAMETER *params: Multiple, Todos los parametros de la función.\n
    RETURNS: Float, tiempo de ejecución de la funcion en milisegundos.\n
    """
    startTime = currentTime() # Current time
    f(*params) # Executes function
    return (currentTime() - startTime) * 1000 # Returns elapsed time in ms

def averageTime(f: Callable, precision: int, *params) -> float:
    """
    Mide el tiempo promedio de ejecución de una función.\n
    PARAMETER f: Function, La función a medir.\n
    PARAMETER *params: Multiple, Todos los parametros de la función.\n
    PARAMETER precision: Integer, cantidad de veces que ejecutar la función. Aumenta la precisión pero tarda mas en devolver resultado.\n
    RETURNS: Float, tiempo promedio de ejecución de la funcion en milisegundos.\n 
    """
    sum = 0 # Suma de todos los tiempos
    for i in range(precision):
        sum += measureTime(f, *deepcopy(params))
    return sum / precision # Suma / Cantidad = Promedio

def quadratic(x: float, a: float, b: float, c: float) -> float:
    """
    Función cuadrática.\n
    f(x) = aX^2 + bX + c\n
    """
    return a * (x**2) + b * x + c

def plotTime(f: Callable, x_values: list, precision: int, measurable: Callable, simulator: Callable):
    """
    Obtiene el tiempo de ejecución promedio de la función measurable() y lo grafica.\n
    Luego, obtiene su curve_fit (Cuadrados minimos) y lo grafica mediante F.\n
    PARAMETER measurable: Function, la función a medir y graficar.\n
    PARAMETER f: La función que utiliza curve_fit para aproximar measurable.\n
    PARAMETER x_values: Las variables independientes a graficar.\n
    PARAMETER precision: La cantidad de ejecuciones de cada variable independiente. Aumenta precisión del promedio.\n
    RETURNS: Nothing. Muestra los gráficos por ventana.\n
    """
    y_values_original = [] # Variables dependientes de la función sin ajustar
    width = digits(x_values[-1]) # Usado exclusivamente para prints

    for i in range(len(x_values)):
        parameters = simulator(x_values[i])
        y_values_original.append(averageTime(measurable, precision, *parameters))
        if debug:
            print(f"{x_values[i]:>0{width}}: {y_values_original[-1]:>07.2f}ms") # Ej: 02900: 45.97ms

    c, pcov = curve_fit(f, x_values, y_values_original) # Obtiene la variación de X/Y en base a F
    y_values_adjusted = [f(n,c[0],c[1], c[2]) for n in x_values] # Obtiene los valores ajustados en base a variación

    if debug:
        print(f"X: {x_values}")
        print(f"Y: {y_values_original}")
        print(f"C: {c}")

    # PLOT
    plt.plot(x_values, y_values_original, label = "Original", c = "Black", linestyle="solid",alpha = 0.5) # Plot original
    plt.plot(x_values, y_values_adjusted, label = f.__name__.title(), c = "Red", linestyle="dashed") # Plot ajustada

    # LABELS
    plt.xlabel("Interval count")
    plt.ylabel("Execution Time (ms)")
    plt.title(f"Average times for {len(x_values) - 1} executions.", loc = 'left')
    
    # X/Y axis marks.
    highestX = x_values[-1]
    highestY = max(arrayMaximum(y_values_original), arrayMaximum(y_values_adjusted))
    xTicks = [round((highestX / 10) * i, 2) for i in range(11)]
    yTicks = [round((highestY / 10) * i, 2) for i in range(11)]
    plt.xticks(xTicks)
    plt.yticks(yTicks)

    plt.legend()
    plt.show() # Muestro el gráfico

def main():
    """
    Si se llama directamente al archivo, ejecuta plotTime().\n
    ARGUMENT 1: Variación entre cada valor de las variables independientes del gráfico.\n
    ARGUMENT 2: Precisión del medidor de promedio.\n
    ARGUMENT 3: Cantidad máxima de las variables independientes.\n
    """
    startTime = currentTime()
    print(f"Running {int(argv[3]) // int(argv[1])} iterations with {argv[2]} precision.")
    interval = [i for i in range(0, int(argv[3]) + 1, int(argv[1]))]
    plotTime(quadratic, interval, int(argv[2]), measurableFunction, simulationFunction)
    print(f"Finished measuring in {currentTime() - startTime}s")
    

if __name__ == '__main__':
    main()