#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

csv1 = pd.read_excel(r"C:\Users\beltr\OneDrive\Documentos\coding\spike_challenge\costo_marginal_programado.xlsx")

csv2 = pd.read_excel(r"C:\Users\beltr\OneDrive\Documentos\coding\spike_challenge\costo_marginal_real.xlsx")
csv2 = csv2.dropna(axis=1)
 
merged_data = pd.merge(csv1, csv2, on=['barra'])
# saving the dataframe  
df.to_csv("costo_marginal.xlsx", index=False) 
print("Merge Creado!!!!")
