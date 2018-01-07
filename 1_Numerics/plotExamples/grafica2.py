# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica2: Graficar una función sencilla

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

# primer lo vamos a hacer usando numpy

x = np.arange(0.0, 6.0, 0.01)
plt.plot(x, [y**2 for y in x]) 
plt.show()

#%%
# ahora lo podemos hacer con listas

x = list()
y = list()
for i in range(0,7): # ojo con range no se pueden utilizar float
    x.append(i)
    
for j in x:
    y.append(j**2)

plt.plot(x,y) 
plt.show()

#%% usando map

x = list()
def cuadrado(h):
    return h*h

for i in range(0,7):
    x.append(i)

y = map(cuadrado, x)

plt.plot(x,y) 
plt.show()

#%% vectorizando la funcion

def cuadrado(h):
    return h*h

x = np.arange(0.0, 6.0, 0.01)

cuadrado_vectorizado = np.vectorize(cuadrado)
y = cuadrado_vectorizado(x)

plt.plot(x,y)
plt.show()

# existe otra posibilidad que es tulizando la función np.pow(), buscar
# cómo funciona y probar su funcionamiento.



