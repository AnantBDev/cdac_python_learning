# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:56:56 2023

@author: anilk
"""
import pandas as pd
df=pd.read_table('http://bit.ly/movieusers',sep="|",header=None);
print(df)
df.info()
df.columns=['userid','age','gender','profile','views']
df['views'].replace(to_replace='[a-zA-Z]{1,}', regex=True, value=0,inplace=True)
print(df)
dfu=pd.unique(df['profile'])
print(dfu)
v_count=pd.value_counts(df['profile'])
import matplotlib.pyplot as plt
plt.pie(v_count,labels=v_count.index,shadow=True,startangle=190,rotatelabels=20)
df['views1']=df['views'].astype(int);
df.views1.mean()

