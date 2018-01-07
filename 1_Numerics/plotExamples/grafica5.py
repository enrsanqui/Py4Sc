# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica5: Error típico en las listas o vectores utilizados

@author: DGReina
"""

import matplotlib.pyplot as plt

l1 = [1, 2, 4, 10, 5]
l2 = [2, 4, 5]

plt.plot(l1, l2)
plt.show()

# modificar l2 añadiendo un valor cualquiera

#%% si trabajamos con vectores

import numpy as np

v1 = np.arange(0,10)
v2 = np.arange(0,10,0.5)

plt.plot(v1, v2)
plt.show()

