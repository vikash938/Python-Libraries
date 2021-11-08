#!/usr/bin/env python
# coding: utf-8

# # Indexes -How to Set, Reset, and Use Indexes

# In[1]:


persson = {
    "first": "Dabbu",
    "last" : "Kumar",
    "email" : "DabbuKumar@gmail.com"
}


# In[2]:


people = {
    "first": ["Dabbu"],
    "last" : ["Kumar"],
    "email" : ["DabbuKumar@gmail.com"]
}


# In[3]:


people = {
    "first": ["Dabbu","Hari","Shree"],
    "last" : ["kumar","Ram", "Ram"],
    "email" : ["DabbuKumar@gmail.com", "HariRam@gmail.com", "ShreeRam@gmail.com"]
}


# In[4]:


people['email']


# In[5]:


import pandas as pd


# In[6]:


df = pd.DataFrame(people)


# In[7]:


df


# In[8]:


df['email']


# In[9]:


type(df['email'])


# In[10]:


df[['last','email']]


# In[11]:


df.columns


# In[12]:


df.iloc[[0,1]]


# In[13]:


df.iloc[[0,1],2]


# In[14]:


df.loc[0]


# In[15]:


df.loc[[0,1],['email','last']]


# In[16]:


df['email']


# In[17]:


# set index for email column
df.set_index('email')


# In[18]:


df


# In[21]:


df.set_index('email', inplace=True)


# In[22]:


df


# In[24]:


df.index


# In[23]:


df.loc['DabbuKumar@gmail.com']


# In[ ]:


df.loc['DabbuKumar@gmail.com','last']


# In[ ]:


# df.loc[0] gives error because 0,1,2 index nolonger available now indexes are 'email'


# In[ ]:


# but df.iloc[0] works same as work before
df.iloc[0]


# In[ ]:


# reset index
df.reset_index(inplace=True)
df


# In[ ]:





# In[ ]:




