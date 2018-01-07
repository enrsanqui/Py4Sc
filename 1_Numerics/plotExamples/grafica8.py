# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica8: Representacion de un diagrma de un barras

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

# vamos a utilizar un diccionario para recordar un poco
dict = {'Dani': 33, 'Antonio': 70, 'Jose': 30, 'Juan': 85} 
for i, key in enumerate(dict): 
    plt.bar(i, dict[key])

# definimos las divisiones de los ejes
#plt.xticks(np.arange(len(dict))+0.4, dict.keys()) # versiones antiguas
plt.xticks(np.arange(len(dict)), dict.keys())
#np.arange(len(dict)) --> define el vector [0, 1, 2, 3] y despues le sumamos 0.4
plt.yticks(dict.values()) 

plt.ylabel("Edad")
plt.xlabel("Profesores")
plt.title("Diagrama de barras")
plt.grid(True)
plt.plot()



