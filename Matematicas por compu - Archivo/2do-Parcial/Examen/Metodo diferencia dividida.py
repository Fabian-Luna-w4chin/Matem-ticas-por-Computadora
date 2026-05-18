import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def tabla_diferencias_divididas(x, y):
    n = len(y)

    tabla = np.zeros([n, n])
    

    tabla[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            numerador = tabla[i+1, j-1] - tabla[i, j-1]
            denominador = x[i+j] - x[i]
            tabla[i, j] = numerador / denominador
            
    return tabla

x = np.array([0.0000, 8.5910, 3.6593, 3.2563, -6.8756, 3.1243, 5.5437, 2.1176, -1.2675, 6.1273, -5.8999, 4.2363], dtype=float)  
y = np.array([0.0000, 8.5910, 3.6593, 3.2563, -6.8756, 3.1243, 5.5437, 2.1176, -1.2675, 6.1273, -5.8999, 4.2363], dtype=float)  

resultado = tabla_diferencias_divididas(x, y)

print("Tabla de Diferencias Divididas:")
print(resultado)

# Graficar
plt.scatter(x, y, label='Datos')
plt.plot(x, y, label='función real', color='red')
plt.legend()
plt.show()

