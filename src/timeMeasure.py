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
from fileUtils import fileCreator, fileReader # Generates disposable data

debug = True

def digits(num):
    """
    Devuelve cantidad de digitos de num.\n
    """
    return len(str(num))

def measureTime(f, *params):
    """
    Mide el tiempo de ejecución de la función.\n
    PARAMETER f: Function, La función a medir.\n
    PARAMETER *params: Multiple, Todos los parametros de la función.\n
    RETURNS: Float, tiempo de ejecución de la funcion en milisegundos.\n
    """
    startTime = currentTime() # Current time
    f(*params) # Executes function
    return (currentTime() - startTime) * 1000 # Returns elapsed time in ms

def averageTime(f, precision, *params):
    """
    Mide el tiempo promedio de ejecución de una función.\n
    PARAMETER f: Function, La función a medir.\n
    PARAMETER *params: Multiple, Todos los parametros de la función.\n
    PARAMETER precision: Integer, cantidad de veces que ejecutar la función. Aumenta la precisión pero tarda mas en devolver resultado.\n
    RETURNS: Float, tiempo promedio de ejecución de la funcion en milisegundos.\n 
    """
    sum = 0 # Suma de todos los tiempos
    for i in range(precision):
        sum += measureTime(f, *params)
    return sum / precision # Suma / Cantidad = Promedio

def quadratic(x, a, b, c):
    """
    Función cuadrática.\n
    f(x) = aX^2 + bX + c\n
    """
    return a * (x**2) + b * x + c

def plotTime(measurable, x_values, precision, f):
    """
    Obtiene el tiempo de ejecución promedio de la función measurable() y lo grafica.\n
    Luego, obtiene su curve_fit (Cuadrados minimos) y lo grafica mediante F.\n
    PARAMETER measurable: Function, la función a medir y graficar.\n
    PARAMETER x_values: Las variables independientes a graficar.\n
    PARAMETER precision: La cantidad de ejecuciones de cada variable independiente. Aumenta precisión del promedio.\n
    PARAMETER f: La función que utiliza curve_fit para aproximar measurable.\n
    RETURNS: Nothing. Muestra los gráficos por ventana.\n
    """
    p_id = datetime.now().microsecond # ID so you can run the program multiple times in paralel
    y_values_original = [] # Variables dependientes de la función sin ajustar

    width = digits(x_values[-1]) # Usado exclusivamente para prints
    for i in range(len(x_values)):
        dt = f"{datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}"
        # Nombro el archivo para poder ejecutar dos instancias del programa sin problema
        file = fileCreator(True, x_values[i], False, outPath=f"Automatic {p_id}-{dt}.txt") # Al usar siempre el mismo archivo no necesito setear semilla
        timestamps, operations = fileReader(file) # Obtiene los parametros utilizados por moleReader
        # NOTA: De reutilizar la función, cambiar linea de arriba
        y_values_original.append(averageTime(measurable, precision, timestamps, operations, []))
        if debug:
            print(f"{x_values[i]:>0{width}}: {y_values_original[-1]:>07.2f}ms") # Ej: 02900: 45.97ms
        deleteFile(file) # Borra el archivo luego de uso.

    c, pcov = curve_fit(f, x_values, y_values_original) # Obtiene la variación de X/Y en base a F
    y_values_adjusted = [f(n,c[0],c[1], c[2]) for n in x_values] # Obtiene los valores ajustados en base a variación

    if debug:
        print(f"X: {x_values}")
        print(f"Y: {y_values_original}")
        print(f"C: {c}")

    # PLOT
    plt.plot(x_values, y_values_original, label = "Original", c = "Black", linestyle="solid", marker='.', alpha = 0.5) # Plot original
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
    plotTime(measurableFunction, interval, int(argv[2]), quadratic)
    print(f"Finished measuring in {currentTime() - startTime}s")
    

if __name__ == '__main__':
    main()