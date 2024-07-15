import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros de la distribución binomial
n = 10
p = 0.3
binomial = stats.binom(n, p)  # Distribución binomial

# Rango de valores x para cubrir la mayor parte de la distribución
x = np.arange(binomial.ppf(0.01), binomial.ppf(0.99))
fmp = binomial.pmf(x)  # Función de Masa de Probabilidad

# Graficar la distribución binomial
plt.plot(x, fmp, '--', color='blue')  # Línea discontinua para la PMF
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)  # Líneas verticales en los puntos
plt.title('Distribución Binomial (n=10, p=0.3)')
plt.ylabel('Probabilidad')
plt.xlabel('Número de accidentes debido a la falta de sueño')
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Cuadrícula en el eje y

# Mostrar la gráfica
plt.show()
