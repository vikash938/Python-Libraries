#!/usr/bin/env python
# coding: utf-8

# # Cleaning Data - Casting Datatypes and Handling Missing Values 

# In[14]:


import pandas as pd
import numpy as np


# In[13]:


people = {
    'first': ['Dabbu', 'Hari', 'Sita', 'Mili', np.nan, None, 'NA'], 
    'last': ['Kumar', 'Ram', 'Ram', 'Kumar', np.nan, np.nan, 'Missing'], 
    'email': ['DabbuKumar@gmail.com', 'HariRam@email.com', 'SitaRam@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['29', '52', '60', '39', None, None, 'Missing']
}


# In[15]:


df = pd.DataFrame(people)

df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)


# In[ ]:


df


# In[5]:


df.dropna()


# In[6]:


# axis = 'index'(here index means row), for columns we put axis = 'columns'
# how = 'any' means any missing value(single value) in a row and columns 
# how = 'all' means all missing value in a row and columns
df.dropna(axis='index', how='any')


# In[7]:


# here subset is column names that were checking for missing values
df.dropna(axis='index', how='any', subset=['email'])


# In[8]:


# here if we want either last name or email
df.dropna(axis='index', how='all', subset=['last','email'])


# In[9]:


df.isna()


# In[10]:


df.fillna(0)


# # Casting Datypes

# In[11]:


df.dtypes


# In[12]:


# this give an error because in columns of age numbers are string not int so that's why it's give an error
df['age'].mean()


# In[ ]:


# convert age column in integers it will give error because we have some nan value in our column
# here we have two option  first if column didn't have any missing value that's work fine not give an error
# second is if in columns have some missing value than either convert those missing value in somerthing else like a zero or convert into float
# but in this case can't convert into zero because we are finding average here 
# so convert into float so nan value stay missing values
df['age'] = df['age'].astype(int)


# In[ ]:


# conert into float so nan value stay missing value
df['age'] = df['age'].astype(float)


# In[ ]:


# we can change all the dataframe type df.astype() pass any argument in this that you want to change
df.dtypes


# In[ ]:


df['age'].mean()


# In[ ]:





# In[ ]:




