# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

Grafica 3d: Ejemplo para hacer gráficas en 3d
    
@authors:DGReina
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # esto falta
from matplotlib import cm
import numpy as np

x=np.arange(-5,5,0.01)
y=np.arange(-5,5,0.01)

figure_3d=plt.figure()
ax=figure_3d.gca(projection='3d')
#Obtenemos las coordenadas resultantes de esos arrays
X,Y=np.meshgrid(x,y)

#Definimos la función cos((x^2+y^2)^1/2)
fxy=np.sqrt(X**2+Y**2)
fz=np.cos(fxy)

#Representamos
ax.plot_surface(X,Y,fz,linewidth=0,cmap=cm.coolwarm)

#ejes
plt.xlabel("$Eje x$")
plt.ylabel("$Eje y$")


#titulo
plt.title("Grafica 3d")