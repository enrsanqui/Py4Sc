# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas1.py: primer script utilizando el módulo pandas. Objetos Series.

@author: DGReina
"""

import pandas as pd
import numpy as np

s1 = pd.Series(["hola", 2, "adios", 4])
print s1

# accedemos al contenido y etiquetas 

print "valores", s1.values
print "etiquetas", s1.index

#%% podemos especificar las etiquetas

l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c", "d"] # el orden de las etiquetas es el mismo orde de la lista o vector

s2 = pd.Series(l1, index= l2)
print s2  

#%% acceso al contenido de la serie

s2 = pd.Series(np.arange(0,10), ["a", "b", "c", "d", "e", "f", "g", "h","i","j"])
print s2
print s2['c'], s2['d'], s2['f']

# podemos utilizar filtros con los indices

trozo = s2[s2 > 5] # esta operación tb la podemos hacer con arrays de numpy
print trozo

#%% convertimos un diccionario en una Serie

diccionario = {"Sevilla": 100, "Cadiz": 40, "Cordoba": 10, "Malaga": 22}
s3 = pd.Series(diccionario)
print s3

#%% como con los diccionarios podemos introducir valores sobre la marcha

diccionario = {"Sevilla": 100, "Cadiz": 40, "Cordoba": 10, "Malaga": 22}
s3 = pd.Series(diccionario)
print s3
s3["jaen"] = 15
print "despues de introducir jaen \n", s3


