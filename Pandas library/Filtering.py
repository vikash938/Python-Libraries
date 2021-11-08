#!/usr/bin/env python
# coding: utf-8

# # Filtering

# In[1]:


# Filtering = Every project by filtering the data that we want from the data that we don't 
people = {
    "first": ["Dabbu","Hari","Shree"],
    "last" : ["kumar","Ram", "Ram"],
    "email" : ["DabbuKumar@gmail.com", "HariRam@gmail.com", "ShreeRam@gmail.com"]
}


# In[2]:


import pandas as pd


# In[3]:


df = pd.DataFrame(people)


# In[4]:


df


# In[5]:


filt = (df['last'] == 'Ram')


# In[6]:


df[filt]


# In[7]:


# another method of filter
df[df['last'] == 'Ram']


# In[8]:


# filt gives us to boolean values of data but when use df.loc[filt] it will give us actual data
df.loc[filt]


# In[9]:


# for email column it will give us to series of emails where the last name is equal to Doe
df.loc[filt, 'email']


# In[10]:


# Other ways to filtering data out using 'and' and 'or' operator not can't use python builtin and,or operator 
# we use ampersand for and = &, for or = |
filt = (df['last'] == 'Ram') & (df['first'] == 'Shree')


# In[11]:


df[filt]


# In[12]:


df.loc[filt, 'email']


# In[13]:


# for  or (|)
filt = (df['last'] == 'Kumar') | (df['first'] == 'Shree')


# In[14]:


df.loc[filt, 'email']


# In[15]:


# when don't want anything that match use(~ = tilde) 
df.loc[~filt, 'email']


# # Add/Remove rows and columns from DataFrame

# In[16]:


df


# In[17]:


df['first'] + ' ' + df['last']


# In[18]:


df['full_name'] = df['first'] + ' ' + df['last']


# In[19]:


df


# In[20]:


df.drop(columns=['first','last'], inplace=True)


# In[21]:


df


# In[22]:


df['full_name'].str.split(' ')


# In[23]:


df


# In[24]:


# want to assign two different columns
df['full_name'].str.split(' ', expand = True)


# In[25]:


# added two new columns
df[['first','last']] = df['full_name'].str.split(' ', expand=True)


# In[26]:


# add single row to data
df.append({'first':'Tony'},ignore_index = True)


# In[27]:


people = {
    "first": ["Tanu","Sher"],
    "last" : ["Shreya",'Rever'],
    "email" : ["TanuSher@comman.com", "Shreya@comman.com"]
}
df2 = pd.DataFrame(people)


# In[28]:


df2


# In[29]:


df = df.append(df2, ignore_index = True)


# In[30]:


df


# In[31]:


df.drop(index=4)


# In[32]:


filt = df['last']=='Ram'
df.drop(index = df[filt].index)


# # sorting Data

# In[33]:


people = {
    "first": ["Dabbu","Hari","Shree",'Sita'],
    "last" : ["kumar","Ram", "Ram", "Ram"],
    "email" : ["DabbuKumar@gmail.com", "HariRam@gmail.com", "ShreeRam@gmail.com", "SitaRam@gamil.com"]
}


# In[34]:


df = pd.DataFrame(people)


# In[35]:


# sort by last name using sort_values()
df.sort_values(by='last')


# In[36]:


# sort by descending order
df.sort_values(by='last', ascending=False)


# In[37]:


df.sort_values(by=['last','first'], ascending=False)


# In[38]:


# sorting lastname by ascending order and firstname in descending order 
df.sort_values(by=['last','first'], ascending=[False,True],inplace=True)


# In[39]:


df


# In[40]:


df.sort_index()


# In[41]:


df['last'].sort_values()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




