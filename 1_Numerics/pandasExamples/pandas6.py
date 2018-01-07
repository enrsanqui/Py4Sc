# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas6.py: operar sobre el Dataframe, nuevas columnas, operaciones entre columnas,
filtrar

@author: DGReina
"""

import pandas as pd

sensores = pd.read_csv("medidas.csv", sep =';', names = ["S1", "S2", "S3"])
# no confundir names con header, header es un entero

#%% vamos a crear un nuevo sensor S4 = S1 + S3

sensores['S4'] = sensores['S1'] + sensores['S3']

print sensores


#%% filtrando por los valores de cierta columna

sen2 = sensores[sensores['S1'] > 10.0]

print sen2

#%% recordar que las series tb se podian filtrar

print sensores['S1'][sensores['S1']> 10.0]

#%% podemos crear un nuevo dataframe que sólo incluya ciertas columnas

nuevo_data = sensores.filter(['S1', 'S2'])

print nuevo_data 

#%% otra forma

nuevo_data2 = sensores[['S1','S2']]

print nuevo_data2
