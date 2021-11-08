#!/usr/bin/env python
# coding: utf-8

# # Pandas basic and slicing

# In[1]:


import pandas as pd
 


# In[2]:


df = pd.read_csv('data_1/survey_results_public.csv')


# In[3]:


#to show starting rows
df.head()


# In[4]:


# to show last five rows
df.tail()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[8]:


df


# In[9]:


schema_df = pd.read_csv('data_1/survey_results_schema.csv')


# In[10]:


schema_df


# In[11]:


df.head()


# In[12]:


df.shape


# In[13]:


df.columns


# In[14]:


df['Hobbyist']


# In[15]:


df['Hobbyist'].value_counts()


# In[16]:


# another method to count in particular column and just like that using python script to find value_counts()
countYes = 0
countNo = 0
for i in df['Hobbyist']:
    if i == 'Yes':
        countYes+=1
    else:
        countNo += 1
print(countYes)
print(countNo)
    


# In[17]:


df.loc[0]


# In[18]:


df.loc[[0,1,2,3], 'Hobbyist']


# In[19]:


#using slicing
df.loc[0:2, 'Hobbyist']


# In[20]:


df.loc[0:2, 'Hobbyist':'Employment']


# In[21]:


df = pd.read_csv('data_1/survey_results_public.csv',index_col='Respondent')
schema_df = pd.read_csv('data_1/survey_results_schema.csv', index_col = 'Column')


# In[22]:


df.head()


# In[23]:


schema_df


# In[24]:


schema_df.loc['MgrIdiot']


# In[25]:


# for only QuestionText
schema_df.loc['MgrIdiot','QuestionText']


# In[26]:


# FOR Sorting 
# for descending order use df.sort_index(ascending=True)
# for permanent sorting use df.sort_index(inplace = True) 
schema_df.sort_index(inplace = True)


# In[27]:


schema_df


# In[28]:


high_salary = (df['ConvertedComp'] > 70000)


# In[29]:


df.loc[high_salary]


# In[30]:


df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']] 


# In[31]:


# filter specific countries
countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countries)


# In[32]:


df.loc[filt, 'Country']


# In[33]:


df['LanguageWorkedWith']


# In[34]:


# to know language specific
filt =  df['LanguageWorkedWith'].str.contains('Python', na=False)


# In[35]:


df.loc[filt, 'LanguageWorkedWith']


# In[36]:


df.rename(columns = {'ConvertedComp' : 'SalaryUSD'}, inplace = True)


# In[37]:


df['SalaryUSD']


# In[38]:


df['Hobbyist']


# In[39]:


df['Hobbyist'].map({'Yes':True, 'No':False})


# In[40]:


df


# In[41]:


df['Hobbyist'] = df['Hobbyist'].map({'Yes':True, 'No':False})


# In[42]:


df


# In[43]:


df.sort_values(by=['Country','SalaryUSD'],ascending = [True,False], inplace=True)


# In[44]:


# if wanted to access multiple columns in then put into a list
df[['Country','SalaryUSD']].head(50)


# In[45]:


# ten highest salay 
df['SalaryUSD'].nlargest(10)


# In[46]:


# largest salary 
df.nlargest(10,'SalaryUSD')


# In[47]:


# smallest salary
df.nsmallest(10, 'SalaryUSD')

