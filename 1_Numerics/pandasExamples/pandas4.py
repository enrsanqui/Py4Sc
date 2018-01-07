# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas4.py: eliminar contenido de los dataframe, más sobre acceso al contenido.

@author: DGReina
"""

import pandas as pd


datos = { "ciudad" : ["Sevilla", "Cadiz", "Malaga"], "ano": [2013,2014,2015], "poblacion" : [0.6, 0.5, 0.3] }
df = pd.DataFrame(datos)

print df

del df['ano']

print "Eliminamos la columna ano \n", df

#%% MÁS SOBRE ACCESO AL CONTENIDO

datos = { "ciudad" : ["Sevilla", "Cadiz", "Malaga"], "ano": [2013,2014,2015], "poblacion" : [0.6, 0.5, 0.3] }
df = pd.DataFrame(datos)

# podemos acceder a un dato concreto columna-fila
print df['ciudad'][2]
print df['ano'][1]
print df['poblacion'][0]

#%% podemos también acceder a dos columnas a la vez

datos = { "ciudad" : ["Sevilla", "Cadiz", "Malaga"], "ano": [2013,2014,2015], "poblacion" : [0.6, 0.5, 0.3] }
df = pd.DataFrame(datos)
print df[['ciudad', 'poblacion']] # hay que pasarle el indice como una lista



#%% copiar columnas --> no están enlazadas 

datos = { "ciudad" : ["Sevilla", "Cadiz", "Malaga"], "ano": [2013,2014,2015], "poblacion" : [0.6, 0.5, 0.3] }
df = pd.DataFrame(datos)

df['parados'] = df['poblacion']
print df 

df['parados'] = [0, 0, 0]
print df 



