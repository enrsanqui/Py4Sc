# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas5.py: convertir los datos de un .csv en un Dataframe. Algunas operaciones
sencillas

@author: DGReina
"""

import pandas as pd
import numpy as np

sensores = pd.read_csv("medidas.csv", sep =';')

print sensores

# hasta aquí tenemos los tres sensores, una Serie por sensor

#%% vamos a incluir unos "hedaers"

sensores = pd.read_csv("medidas.csv", sep =';', names = ["S1", "S2", "S3"])
# no confundir names con header, header es un entero

print sensores

#%% podemos hacer la media, desviación, máx, etc.

media = list()
media.append(np.mean(sensores["S1"].values))
media.append(np.mean(sensores["S2"].values))
media.append(np.mean(sensores["S3"].values))

print media

#%%
# otra forma

media2 = [np.mean(sensores["S1"].values), np.mean(sensores["S2"].values), np.mean(sensores["S3"].values)]

print media2

#%% iterando sobre columnas

media3 = list()
for colname, col in sensores.iteritems():
    media3.append(np.mean(col.values))

print media3

#%% list comprenhension

media4 = [np.mean(j.values) for i, j in sensores.iteritems()]

print media4

# ¿Por qué j.values y no j.values()?
# ¿Por qué sensores.iteritems() y no sensores.iteritems?

#%% método describe, información estadística de las columnas

print sensores.describe()