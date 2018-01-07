# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

grafica14: Ejemplo para hacer gráficas en 2d
    
@authors:DanyGR MarioDM IgnacioGP
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-5,5,0.01)
y=np.arange(-5,5,0.01)

#Obtenemos las coordenadas resultantes de esos arrays
X,Y=np.meshgrid(x,y)
#print X, Y

#Definimos la función cos(x^2+y^2)
fxy=np.cos(X**2+Y**2)

#Representamos
plt.contourf(X,Y,fxy)

#Añadimos una colorbar
plt.colorbar()

plt.axis('square')
plt.axis([-5,5,-5,5])


#ejes
plt.xlabel("Eje x")
plt.ylabel("Eje y")

#titulo
plt.title("Grafica 2d")