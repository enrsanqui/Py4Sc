# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas3: introducción a los dataframes.

@author: DGReina
"""

import pandas as pd

# definimos un diccionario en el que cada posición es un array
datos = { "ciudad" : ["Sevilla", "Cadiz", "Malaga"], "ano": [2013,2014,2015], "poblacion" : [0.6, 0.5, 0.3] }

df = pd.DataFrame(datos)
print df

#%%
# si queremos especificar el orden las columnas

df = pd.DataFrame(datos, columns = ["poblacion", "ciudad","ano"])
print df

#%% si no existen los datos los pone como NaN

datos = { "ciudad" : ["Sevilla", "Cadiz", "Malaga"], "ano": [2013,2014,2015], "poblacion" : [0.6, 0.5, 0.3] }
df = pd.DataFrame(datos, columns = ["poblacion", "ciudad","ano","municipios"])
print df

#%%
# podemos introducir los valores sobre la marcha

df["municipios"] = [50, 22, 24]
print df

#%% podemos espcificar los indices también

df = pd.DataFrame(datos, columns = ["poblacion", "ciudad","ano","municipios"], index= ['a', 'b','c'])
df["municipios"] = [50, 22, 24] # si quitamos esta línea municipios no está definido
print df


#%% ACCESO A LA INFORMACIÓN 
# podemos acceder de dos formas mediante "."+nombre o ["nombre"]

print df.poblacion
print df["poblacion"]

#%% podemos filtrar como hemos hecho antes con las Series

datos = df[df["poblacion"] > 0.5]
print datos
