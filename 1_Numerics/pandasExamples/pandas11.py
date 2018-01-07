# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas11.py: Inspección de un dataframe para machine learning

@author: DGReina
"""

import pandas as pd

datos = pd.read_csv('house_data_small.csv', low_memory=False, sep=',')
print datos.shape # (filas, columnas)

print datos.columns # ver las columnas 

print datos.info()

#%% obetener algunas filas solo

print datos.head(5) # nos mostrará las primera 5 líneas

#%% también podemos enpezar por abajo

print datos.tail(2)

#%% slicing utilizando el método iloc

print datos.iloc[0:1, 0:3] # funciona igual que el slicing the numpy
 # [slicing filas, slicing columnas]
 

