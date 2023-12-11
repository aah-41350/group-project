#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:25:32 2023

@author: azfar
"""
import pandas as pd

filepath = '/Users/azfar/Documents/GitHub/group-project/Data Files'

# For Total Administered Vaccinations
df_totalvax = pd.read_csv(filepath+'/for_analysis.csv',
                          usecols=['vaxtype','total_doses'])
df_totalvax.drop(3, axis='index', inplace=True)
df_totalvax.to_csv(filepath+'/total_pfi-ast-sin.csv', index=False)

# For Serious AEFI by Brands
df_serious = pd.read_csv(filepath+'/aefi_serious.csv')
df_serious.drop(columns='date', inplace=True)

vaxgroups = df_serious.groupby('vaxtype')
pfizer = vaxgroups.get_group('pfizer').drop(columns='vaxtype').sum()
astrazeneca = vaxgroups.get_group('astrazeneca').drop(columns='vaxtype').sum()
sinovac = vaxgroups.get_group('sinovac').drop(columns='vaxtype').sum()

df_aefi = pd.DataFrame({
    'Pfizer' : pfizer,
    'Astra' : astrazeneca,
    'Sinovac' : sinovac,
    })
df_aefi = df_aefi.T
df_aefi.to_csv(filepath+'/serious_aefi.csv')

df1 = pd.read_csv(filepath+'/total_pfi-ast-sin.csv')
df2 = pd.read_csv(filepath+'/serious_aefi.csv')

df2.columns=['vaxtype','suspected_anaphylaxis','complete_facial_paralysis',
             'venous_thromboembolism','myo_pericarditis']

df3 = pd.merge(left=df1, right=df2, how='inner')
df3.to_csv(filepath+'/serious-aefi-edit.csv', index=False)