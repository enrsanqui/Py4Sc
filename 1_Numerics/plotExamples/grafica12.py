# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica12: uso de matplotlib orientado a objetos

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(0,2*np.pi,(2*np.pi/100))
y = np.sin(x)
y2 = np.cos(x)
fig1 = plt.figure() 
ax1 = fig1.add_subplot(111) # ax1 es un objeto de tipo figura 
ax1.plot(x,y)
ax1.plot(x,y2)
ax1.set_xlabel("X") # ahora los métodos cambian un poco, antes era plt.xlabel
ax1.set_ylabel("Y")
ax1.set_xlim(0, 2*np.pi) # báicamente tenemos que añadir set_
ax1.set_ylim(-1.1, 1.1)
ax1.set_title("Grafica 1")
ax1.legend(["seno", "coseno"]) # algunos métodos son los mismos, que lio!! :(
plt.show()

#%matplotlib qt
