# -*- coding: utf-8 -*-
"""
Python: Machine Learning, Optimización y Aplicaciones, 2017
  
Grafica 13: Diagrama circular 
        
@authors:DGReina
"""

import matplotlib.pyplot as plt

visitas=[43.5,35.7,3.62,100.5,20.0,46.0]
paises=[u'España',u'México','Francia','USA','Suiza','Italia']
explode=[0.05,0,0,0,0,0.05] # separación de cada una de las porciones
plt.pie(visitas,labels=paises,explode=explode)
plt.title("Porcentajes de visitas")