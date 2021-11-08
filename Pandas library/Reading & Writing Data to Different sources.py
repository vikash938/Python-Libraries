#!/usr/bin/env python
# coding: utf-8

#  # Reading/Writing Data to Different Sources - Excel, JSON, SQL, Etc
# 

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('data_1/survey_results_public.csv', index_col = 'Respondent')
schema_df = pd.read_csv('data_1/survey_results_schema.csv', index_col = 'Column')


# In[3]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[4]:


df.head()


# In[5]:


filt = (df['Country'] == 'India')
india_df = df.loc[filt]
india_df.head()


# In[6]:


# if want to export this new filter dataframe to csv file use to_csv
india_df.to_csv('data_1/modified.csv')


# In[7]:


# tab delimited file (tab separated values)
india_df.to_csv('data_1/modified.tsv', sep='\t')


# In[8]:


# new filter dataframe convert into excel file 
india_df.to_excel('data_1/modified.xlsx')


# In[10]:


test = pd.read_excel('data_1/modified.xlsx',index_col= 'Respondent')


# In[12]:


test.head()


# In[15]:


# write our modified dataframe to a JSON file method we used is to_json
# orient = 'records' which is  list like 
india_df.to_json('data_1/modified.json', orient = 'records', lines = True)


# In[17]:


#reading json file
test = pd.read_json('data_1/modified.json', orient = 'records', lines = True)


# In[18]:


test.head()


# In[22]:


# read and write data from SQL 
# for this  you have to intsall this libraries 
from sqlachemy import create_engine
import psycopg2


# In[ ]:


engine = create_engine('postgresql://dbusername:dbpassword@localhost:5432/sample_db')
india_df.to_sql('sample_table',engine)


# In[ ]:


india_df.to_sql('sample_table',engine, if_exists='replace')


# In[ ]:


sql_df = pd.read_sql('sample_table',engine, index_col='Respondent')


# In[ ]:


sql_df.head()


# In[ ]:


sql_df = pd.read_sql_query('SELECT * FROM sample_table',engine, index_col='Respondent')


# In[ ]:


sql_df.head()


# In[ ]:


# we can read data from url also
post_df = pd.read_json('url')


# In[ ]:


post_df.head()

