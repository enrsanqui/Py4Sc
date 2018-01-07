# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas7.py: matplotlib y pandas.

@author: DGReina
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("medidas.csv", sep =';', names = ["S1", "S2", "S3"])

x = np.arange(0, len(datos['S1']))

plt.figure(1, figsize=(5,7))
plt.subplot(311)
plt.scatter(x,datos['S1'], color = 'r')
plt.subplot(312)
plt.scatter(x,datos['S2'], color = 'b')
plt.subplot(313)
plt.scatter(x,datos['S3'], color = 'k')
plt.show

# poner títulos a los ejes y a las gráficas
# limitar las graficas a los valores máximos, .xlim e .ylim
# activar la rejilla.


#%% Los data frames tb tienen sus propios métodos para visualizar los datos
# UFFFSSSSSSS demasiadas formas de hacer lo mismo. 

datos.plot()

#%% Incluso para cada Serie

#datos['S1'].plot()
datos['S1'].hist()


