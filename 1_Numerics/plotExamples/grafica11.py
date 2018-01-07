# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica11: Subplot, diagrama de barras horizontal y tamaño de las figuras 

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0,10,10)
y = np.random.randint(0,10,10)

plt.figure(figsize= (10,10)) # podemos definir muchas cosas entre ellas el tamaño

plt.subplot(221) # aquí lo importante es el número
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Grafica 1")

plt.subplot(222)
plt.scatter(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Grafica 2")

plt.subplot(223)
plt.bar(x,y) 
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.title("Grafica 3")

plt.subplot(224)
plt.barh(x,y) # diagra ma barras horizontal, funciona igual
plt.xlim([min(x), max(x)]) # definir los limites de los ejes, tb exist ylim
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Grafica 4")

# los valores por defecto que utilizan plt.figure() están guardados
# como un diccionario

print "Tam por defecto", plt.rcParams['figure.figsize']
print "Resolución por defecto", plt.rcParams['figure.dpi']

 