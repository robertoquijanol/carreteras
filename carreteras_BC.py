# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:00:31 2020

@author: rober
"""

import pandas as pd
#%%
bc_csv = pd.read_csv('bc_carreteras.csv')
#%%
print("El numero de registros en BC es:")
print(len(bc_csv['entidad_federativa']))
#%%
municipios_bc = bc_csv['municipio'].value_counts().to_frame('count').sort_index()
print("Por municipio:")
print(municipios_bc)
#%%
accesibilidad = bc_csv['grado_accesibilidad'].value_counts().to_frame('count').sort_index()
print("Por accesibilidad:")
print(accesibilidad)
#%%
por_municipio = bc_csv.groupby(['municipio', 'grado_accesibilidad']).size().sort_index()
print(por_municipio)
por_municipio.to_csv('carreteras_por_municipio.csv')
#%%