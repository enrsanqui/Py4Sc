# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017

pandas2.py: trabajando con series en las que faltan datos y filtrando.

@author: DGReina
"""

import pandas as pd
import numpy as np


s = pd.Series([1,3,5,np.nan,6,8])
print s

# comprobar que un elemento es Nan

print pd.isnull(s)

# Cuando leemos datos de archivos puedens ser que falten datos
# y que se rellenen con Nan

# filtrado!!! ESTO ES MUY POTENTE!!

s1 = s[pd.isnull(s) == False] 

print s1

s2 = s[s > 5] # filtro los elementos mayores de 5

print s2

#%% podemos sustituir los valos Nan por otros valores

import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])
print s

print s.fillna(value = 0)

#%% método apply lo utilizaréis mucho en ML

import pandas as pd
import numpy as np

def cuadrado(a):
    return a * a

v1 = np.arange(10)
s3 = pd.Series(v1)

print s3 # Serie original

s4 = s3.apply(cuadrado) # se crea una nueva Serie, la original no se modifica

print s4

#%% podems utilizar una función lambda

s5= s3.apply(lambda x: x**3)

print s5

