# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica6: Representacion de un histograma

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

numeros = np.random.randn(1000)
#plt.hist(numeros)
plt.hist(numeros, bins = 15) # Ahora le indicamos el número de barras 
# que queremos añadir
plt.show()

#%% representar muestras de una distribución normal

y= np.random.normal(10, 5, 1000)
plt.hist(y)
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Distribucion normal media=10")
plt.plot()


#%% representar muestras de una distribución exponencial

y= np.random.exponential(3, 1000)
plt.hist(y)
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Distribucion Exponencial")
plt.plot()

#%% ahora vamos a leer los datos de un archivo

f = open('numeros.txt')

l1 = list()
for num in f:
    l1.append(int(num))

n1 =np.asanyarray(l1) # lo convertimos en un array ... nos puede interesar
#plt.hist(l1)
plt.hist(n1)
plt.show()

# ejercicio: hacer lo mimos utilizando la función np.loadtxt


#%% totalmente aleatorio

import random

lista = list()

"""
for i in range(1000):
    lista.append(random.random())
"""

plt.hist([random.random() for i in range(1000)])












