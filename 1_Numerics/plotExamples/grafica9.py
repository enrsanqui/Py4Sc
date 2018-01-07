# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica9: Gráfica con barra de errores

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4, 0.2) # vector de x
y = np.exp(-x) # función que vamos a representar
np.random.seed(1)
e1 = 0.1 * np.abs(np.random.randn(len(y)))  # el error lo sacamos aleatoriamente
error_maximo = max(list((e1)))
ind_error = list(e1).index(error_maximo)
print error_maximo, x[ind_error]
plt.errorbar(x, y, yerr=e1, fmt='.-')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Grafica con barra de errores")
plt.annotate(u'Error máximo', xy=(x[ind_error], error_maximo+e1[ind_error]), xytext=(1.3, 1), arrowprops=dict(facecolor='black', shrink=0.05),)
#plt.text(1, 1, "grafica")
plt.show()




