# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica3: Rejilla, ejes y más cosillas 

@author: DGReina
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 6.0, 0.01)

plt.figure(figsize=(10,10))
plt.plot(x, [y**2 for y in x])
plt.grid(True) # activamos el grid o rejilla

plt.axis([0, 6, 0, 36]) # hay que definir los límites para los dos ejes  
# [xmin, xmax, ymin, ymax]
# podríamos haber utilizado max(x) para definir xmax ... si no sabemos el máximo

# ejes
plt.xlabel("Eje x")
plt.ylabel("Eje y")

# titulo
plt.title("Grafica 1")

# legenda
plt.legend(["Leyenda"]) 

# grabamos la imagen
plt.savefig("Figura1.png") # el formato se lo damos automáticamente 

plt.show()

