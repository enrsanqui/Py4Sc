# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas8.py: experimento de contactos y filtrado

@author: DGReina
"""

import pandas as pd
import matplotlib.pyplot as plt

col = ["emisor", "receptor","t_inicio", "t_final","no_uso1", "no_uso2"]
datos = pd.read_table('upb2011.dat', names = col) # otra forma de leer datos


#%% distribución de la duración los contactos

datos['duracion'] = datos["t_final"] - datos["t_inicio"]
plt.figure()
plt.hist(datos['duracion'], bins = 100) # distribución exponencial
plt.xlabel("Time [s]")
plt.ylabel("Frequency")
plt.show()


#%% eliminamos los datos de los contactos que son 0

datos2 = datos[datos['duracion']>0]

plt.figure()
plt.hist(datos2['duracion'], bins = 100) # distribución exponencial
plt.show()

#%% la duracion de los contactos de un nodo determinado

nodo = 1 # podemos cambiar el nodo
datos_nodo1 = datos[datos['emisor'] == nodo]
datos_nodo1_nuevo = datos_nodo1[datos_nodo1['duracion']>0]
plt.figure()
plt.hist(datos_nodo1_nuevo['receptor'], bins = 100) 
plt.show()

#%% Duracion entre los contactos de dos nodos

emisor = 1
receptor = 23

datos_pareja = datos[datos['emisor'] == emisor]
datos_pareja = datos_pareja[datos_pareja['receptor']== receptor]

datos_pareja["duracion"].hist()
# sólo hay dos contactos

