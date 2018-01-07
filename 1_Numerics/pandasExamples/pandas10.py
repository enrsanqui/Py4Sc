# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas10.py: Inspeccionar DataFrames

@author: DGReina
"""

import pandas as pd

col = ["emisor", "receptor","t_inicio", "t_final","no_uso1", "no_uso2"]
datos = pd.read_table('upb2011.dat', names = col) # otra forma de leer datos

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
