# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica7: Representacion de un diagrama de dispersión

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.random.randn(1000) # vectores de numeros aleatorios
x = np.arange(0,1000,1)
plt.scatter(x,y)
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Diagrama de dispersion")
plt.plot()


