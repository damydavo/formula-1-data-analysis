#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


results = pd.read_csv('results.csv')
races = pd.read_csv('races.csv')
drivers = pd.read_csv('drivers.csv')
constructors = pd.read_csv('constructors.csv')


# In[4]:


df = pd.merge(results, races[['raceId', 'year', 'name', 'round']], on = 'raceId', how = 'left')
df = pd.merge(df, drivers[['driverId', 'driverRef', 'nationality']], on = 'driverId', how = 'left')
df = pd.merge(df, constructors[['constructorId', 'name', 'nationality']], on = 'constructorId', how = 'left')


# In[5]:


df.shape


# In[6]:


df


# In[7]:


# drop columns

df.drop(['number', 'position', 'positionText', 'laps', 'fastestLap', 'statusId', 'resultId', 'raceId', 'driverId', 'constructorId'], axis=1, inplace=True)


# In[8]:


df.head()


# In[9]:


df.shape


# 

# In[10]:


df.rename(columns={'rank': 'fastestLapRank', 'name_x': 'gpName', 'nationality_x': 'driverNationality', 'name_y': 'constructorName', 'nationality_y' : 'constructorNationality', 'driverRef': 'driver'}, inplace=True)


# In[11]:


df.head()


# In[12]:


# rearrange column
df.columns


# In[13]:


df=df[['year', 'gpName', 'round', 'driver', 'constructorName', 'grid', 'positionOrder', 'points', 'time', 'milliseconds', 'fastestLapRank', 
      'fastestLapTime', 'fastestLapSpeed', 'driverNationality', 'constructorNationality']]


# In[14]:


df.head()


# In[15]:


df


# In[16]:


df.describe()


# In[17]:


df = df[df['year']!=2019]


# In[18]:


df.head()


# In[19]:


# sort values
df = df.sort_values(by=['year', 'round', 'positionOrder'], ascending = [False, True, True])


# In[20]:


df.head()


# In[22]:


# replace /N values in the time column with NAN
df.time.replace('\\N', np.nan, inplace=True)
df.milliseconds.replace('\\N', np.nan, inplace=True)
df.fastestLapRank.replace('\\N', np.nan, inplace=True)
df.fastestLapTime.replace('\\N', np.nan, inplace=True)
df.fastestLapSpeed.replace('\\N', np.nan, inplace=True)


# In[23]:


# change datatypes
df.fastestLapSpeed = df.fastestLapSpeed.astype(float)
df.fastestLapRank = df.fastestLapRank.astype(float)
df.milliseconds = df.milliseconds.astype(float)


# In[24]:


# reset index
df.reset_index(drop=True, inplace=True)


# In[25]:


df.shape


# In[26]:


df.info()


# In[ ]:




