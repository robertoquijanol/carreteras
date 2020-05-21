# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:39:05 2020

@author: rober
"""


import pandas as pd
#%%
mexico_csv = pd.read_csv('carreteras.csv')
bc_carreteras = 'bc_carreteras.csv'
#%%
mexico_csv.head()
#%%
print("El numero de registros utilizados es:")
print(len(mexico_csv['entidad_federativa']))
#%%
grado_accesibilidad = mexico_csv['grado_accesibilidad'].value_counts().to_frame('count').sort_index()
print("Los grados de accesibilidad son:")
print(grado_accesibilidad)
#%%
por_entidades = mexico_csv['entidad_federativa'].value_counts().to_frame('count').sort_index()
print("El numero registrado por estado:")
print(por_entidades)
#%%
estados_csv = pd.read_csv('carreteras.csv', index_col='entidad_federativa')
#%%
bc = estados_csv.loc['Baja California']
print(bc)
bc.to_csv(bc_carreteras)
#%%
