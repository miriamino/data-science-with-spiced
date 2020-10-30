import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('../data/TG_STAID002759.txt', header=14)
df.set_index(pd.to_datetime(df['    DATE'], format='%Y%m%d'), inplace=True)
df = pd.read_csv('../data/TG_STAID002759.txt', header=14)
df.columns = df.columns.str.replace(' ', '')
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d')
df.set_index(df['DATE'], inplace=True)
df['TG'] = df['TG'].replace({-9999 : np.nan })
df['temp'] = df['TG']
df = df[['temp']].copy()
df.sort_index(inplace= True)

#create test df
df_test = df['2019-10':].copy()
#create train df
df_train = df[:'2019-09'].copy()

df_train['temp'] = df_train['temp'].fillna(df_train['temp'].mean())

df.to_csv('cleantemp.csv')