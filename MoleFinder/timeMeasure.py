from matplotlib import pyplot as plt
import time
import sys
import os
import seaborn as sns
import numpy as np
import scipy as sp

# Codigo robado que bloquea prints
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

# Ejecuta FUNCTION con PARAMS, devuelve el tiempo de ejecución
def measureTime(function, *params):
    startTime = time.time()
    with HiddenPrints():
        function(*params)
    return time.time() - startTime

# Mide el tiempo de ejecución de FUNCTION con PARAMS, ITERATIONS veces y devuelve el promedio
def averageTime(function, *params, iterations):
    sum = 0
    for i in range(iterations):
        sum += measureTime(function, *params)
    return sum / iterations

# Siempre seteamos la seed de aleatoridad para que los resultados sean reproducibles
np.random.seed(12345)

sns.set_theme()

points = ((0, 0), (1, 0.75), (2, 2.25))
x = [point[0] for point in points]
y = [point[1] for point in points]

ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, y, "bo")
ax.set_ylim(-0.1, 2.5)
ax.set_xlim(-0.1, 2.5)

f = lambda x: 1.125 * x  - 0.125
ax.plot([p[0] for p in points], [f(p[0]) for p in points], 'r')

plt.show()

None