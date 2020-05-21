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
#%%
municipios_bc['alta'] = int(accesibilidad.loc['Accesibilidad alta'])
#%%
municipios_bc['baja'] = int(accesibilidad.loc['Accesibilidad baja'])
#%%
municipios_bc['media'] = int(accesibilidad.loc['Accesibilidad media'])
#%%
municipios_bc['muy alta'] = int(accesibilidad.loc['Accesibilidad muy alta'])
#%%
municipios_bc['muy baja'] = int(accesibilidad.loc['Accesibilidad muy baja'])
#%%
print(municipios_bc)
#%%
alta = int(accesibilidad.loc['Accesibilidad alta'])
#%%