#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:24:07 2023

@author: azfar
"""

import pandas as pd
import numpy as np

filepath = '/Users/azfar/Documents/GitHub/group-project/Data Files'

# Import original datasets into specified DataFrames
df = pd.read_csv(filepath+'/for_analysis.csv')

# Distribution of vaccine brands
total_allvax = df['total_doses'].sum()

print(df['total_doses'].loc[3])
pct_pfizer = 45070100 / total_allvax * 100
pct_astra = 5708790 / total_allvax * 100
pct_sinov = 21584481 / total_allvax * 100
pct_sinop = 44309 / total_allvax * 100

print(pct_pfizer + pct_astra + pct_sinop + pct_sinov)