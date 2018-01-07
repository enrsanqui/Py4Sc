# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica10: Diagrama de barras con errores utilizando un .cvs con los datos

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

# paso 1: leo el archivo, el archivo tiene las medidas de tres instrumentos
# separadas en columnas

v1 = np.loadtxt("medidas.csv", delimiter=';')

medias = np.mean(v1, axis = 0) # axis 0, trabajamos con columnas!!!
desviaciones = np.std(v1, axis = 0)
x = np.arange(0,3,1)

# ahora calculamos los intervalos de confianza del 95%
# media +/- desviación * 1.96 / sqrt(N)
intervalo_sup = medias + (desviaciones * 1.96 / np.sqrt(len(v1[0])))
intervalo_inf = medias - (desviaciones * 1.96 / np.sqrt(len(v1[0]))) 

deltas_error = intervalo_sup - intervalo_inf
# vamos a dibujarlo como diagrama de barras

plt.bar(x, medias, color = 'y', yerr = deltas_error)
plt.xlabel("Instrumentos")
plt.ylabel("Medida")
plt.xticks(x, ["Inst1", "Inst2", "Inst3"]) # Definimos los xticks
plt.grid(True)
plt.title("Diagrama de barras con intervalos de confianza")
plt.show()

# Ejercicio que se propone: utilizar el codigo para calcular los intervalos de
# confianza y pasarlo a una función y generalizarlo para cualquier tamaño.
# Crear un archivo .csv distinto al usado en el ejemplo y comprobar que
# funciona.
