# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas9.py: ordenar dataframes por una columna.

@author: dany
"""

import pandas as pd


col = ["sensor1", "sensor2", "sensor3"]
datos = pd.read_table('medidas.csv', names = col, delimiter =";")

datos_orden_s1 = datos.sort_values(by='sensor1')
print datos
print datos_orden_s1

#%% por defecto el orden es ascendente si lo queremos cambiar

datos_orden_s1 = datos.sort_values(by='sensor1', ascending = False)

print datos_orden_s1


