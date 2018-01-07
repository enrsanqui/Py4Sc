# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica4: Dibujar varias funciones en una misma figura y decorar las figuras

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.01)
f1 = x*x
f2 = x*x*x

plt.plot(x,f1,'r') # 'r' para dibujar en color rojo
plt.plot(x,f2,'b') # 'b' para dibujar en color azul

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Varias funciones en una misma figura")
plt.legend(["x^2", "x^3"], loc = "upper center")

# si seguimos añadiendo funciones todas se incluira en la misma
#figura

#%% otra forma de trabajar podemos especificar color, tipo de linea
# marcadores

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1, 1, 0.10) # lo cambiamos para que se vean mejor los marcadores
f1 = x*x
f2 = x*x*x

plt.plot(x,f1,color ='r', linestyle='--', marker = 'o') 
plt.plot(x,f2,color ='b', linestyle=':', marker = 'o') 
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Varias funciones en una misma figura")
plt.legend(["x^2", "x^3"], loc = "upper center")

#linestyle --> definimos el estilo de linea
#color --> definimos el color
#maker --> definimos el marcador
#hay bastantes más ...

