#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
df = pd.read_csv('wide other cites ars 20mo v2.csv')


# In[26]:


df_copy = df.copy()
import warnings
warnings.filterwarnings('ignore')


# In[27]:


df_copy = df_copy[[i for i in df_copy.columns if i.startswith('mo')]]


# In[28]:


import numpy as np
max_value = 240
min_value = -24
row_num = len(df_copy)
columns = list(range(int(min_value), int(max_value) + 1))
zero_array = np.zeros((row_num, len(columns)))
df_temp = pd.DataFrame(zero_array, columns = columns)


# In[29]:


def fill_zeros(col):
    for index, i in enumerate(col):
        if i!= None and not pd.isna(i) and i <=240 and i >= -24:
            i = int(i)
            if not (np.isnan(i)):
                df_temp.loc[index, i] = 1
df_copy.apply(fill_zeros, axis = 0)


# In[30]:


df_temp.columns = ['mo_' + str(i) for i in df_temp.columns]


# In[31]:


df = df[[i for i in df.columns if not i.startswith('mo')]]


# In[32]:


df_temp = df.merge(df_temp, left_index = True, right_index = True, how = 'inner')


# In[33]:


df_temp.to_csv('file.csv', index=False)

