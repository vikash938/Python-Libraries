#!/usr/bin/env python
# coding: utf-8

# # -Grouping and Aggregating - analyzing and Exploring Your Data
#  # -Cleaning data with our data set
#  # -Working woth Date and Time series data

# In[8]:


# Aggregate functions are Mean, Median and Mode


# In[10]:


import pandas as pd


# In[12]:


df = pd.read_csv('data_1/survey_results_public.csv', index_col = 'Respondent')
schema_df = pd.read_csv('data_1/survey_results_schema.csv', index_col = 'Column')


# In[14]:


df.shape


# In[16]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[18]:


df.head()


# In[26]:


df['ConvertedComp'].head(15)


# In[28]:


df['ConvertedComp'].median()


# In[30]:


df.median() 


# In[32]:


df.describe()


# In[34]:


df['ConvertedComp'].count()


# In[36]:


df['Hobbyist']


# In[38]:


df['Hobbyist'].value_counts()


# In[40]:


schema_df.loc['SocialMedia']


# In[42]:


schema_df


# In[44]:


df['SocialMedia'].value_counts()


# In[46]:


#for results in percentage
df['SocialMedia'].value_counts(normalize=True)


# # groupby
# >Specific results based on country or based on other columns ....so we're going to have group....that's why we are using 'groupby' function
# > gruopby Operation = spliting up object + apply function + combine results

# In[48]:


df['Country'].value_counts()


# In[50]:


# df.groupby gives us object (<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000022A8543CDF0>)
df.groupby(['Country'])
# that why we assign this in a variable 
country_grp = df.groupby(['Country'])


# In[52]:


country_grp.get_group('United States')


# In[54]:


country_grp.get_group('India')


# In[55]:


filt =  df['Country'] == 'United States'
df.loc[filt]


# In[56]:


# most popular social media sites broke down by unitedstates
df.loc[filt]['SocialMedia'].value_counts()
# this result is one specific country


# In[57]:


# for DataFrame use group by object it's just like running a filter for all countries....than group these by apply groupby function than apply a function to combine these results
#for country group SocialMedia column...it will give us most popular social media sites broke down by countries
country_grp['SocialMedia'].value_counts().head(50)


# In[58]:


# for particular a country
country_grp['SocialMedia'].value_counts().loc['Russian Federation']


# In[59]:


df['Country'].sort_values(ascending=True)


# In[60]:


# now median of salary column which labeled with ConvertedComp
# median salary of all the countries
country_grp['ConvertedComp'].median()


# In[61]:


# grab a specific country salay (here Country column are indexes)
country_grp['ConvertedComp'].median().loc['Germany']


# In[62]:


# for mean and median together then use 'agg' method
country_grp['ConvertedComp'].agg(['median','mean'])


# In[63]:


# mean, median salary for specific country 
country_grp['ConvertedComp'].agg(['mean','median']).loc['Canada']


# In[64]:


# how many people in each country know how to use python
# let's do for single country using filtering approach
filt = df['Country'] == 'India'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python')


# In[65]:


#to konow how many knew python in india using  sum method(sum method work with numerical data as well as boolean also)
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()


# In[66]:


#to know how many knew python from each country 
country_grp['LanguageWorkedWith'].str.contains('python').sum()


# In[67]:


# using apply method to do correctway
country_grp['LanguageWorkedWith'].apply(lambda x:x.str.contains('Python').sum())


# In[68]:


# Total number of respondents from each country who respondent the survey
country_respondents = df['Country'].value_counts()
country_respondents


# In[69]:


country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x:x.str.contains('Python').sum())
country_uses_python


# In[70]:


# now we have a variable is a series of total number of people in each country who respondents
# another variable is a series that is the total number of people in each country who knows python
# now combine both series using pandas 'concat'
python_df = pd.concat([country_respondents, country_uses_python], axis = 'columns',sort= False)
python_df


# In[71]:


# some columns here don't relate to each other so let rename it and that they make more sense in the context
python_df.rename(columns = {'Country':'NumRespondents','LanguageWorkedWith':'NumKnowsPyhton'}, inplace=True)


# In[72]:


python_df


# In[73]:


# creating a new column to know percentage who know python
python_df['PctKnowsPython'] = (python_df['NumKnowsPyhton']/python_df['NumRespondents'])*100
python_df


# In[74]:


# sort by percentage who knows python
python_df.sort_values(by='PctKnowsPython',ascending = False, inplace=True)


# In[75]:


python_df.head(50)


# In[76]:


# for specific country details who know python and respondents
python_df.loc['India']


# # Cleaning Data - Casting Datatypes and Handling Missing Values
# 

# In[77]:


#creating a list of missing values 
na_vals = ['NA','Missing']
df = pd.read_csv('data_1/survey_results_public.csv', index_col = 'Respondent', na_values = na_vals)
schema_df = pd.read_csv('data_1/survey_results_schema.csv', index_col = 'Column')


# In[78]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[79]:


df.shape


# In[80]:


df.head()


# In[81]:


# calculate the average number of years of coding experience 
# Compare experience against average
# unique values 
df['YearsCode'].unique()


# In[82]:


df['YearsCode'].replace('Less than 1 year',0, inplace=True)


# In[83]:


df['YearsCode'].replace('More than 50 years',51, inplace=True)


# In[84]:


df['YearsCode'] = df['YearsCode'].astype(float)


# In[85]:


df['YearsCode'].mean()


# In[86]:


df['YearsCode'].median()


# # Working with Dates and Time Series Data

# In[87]:


# here is cryptocurrency data 
import pandas as pd


# In[88]:


# data frame to load datetime
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv(r"C:\Users\Vikash Kumawat\Desktop\ETH_1h.csv", parse_dates=['Date'], date_parser=d_parser)


# In[89]:


df.head()


# In[90]:


df.loc[0,'Date']


# In[91]:


df.loc[0,'Date'].day_name()


# In[92]:


# for parse the date  (this conversion we can do in reading csv file)
df['Date'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d %I-%p')


# In[93]:


df['Date']


# In[94]:


# to day name
df.loc[0,'Date'].day_name()


# In[95]:


# to entire column day name
df['Date'].dt.day_name()


# In[96]:


#new column of day name
df['DayOfWeek'] = df['Date'].dt.day_name()


# In[97]:


df


# In[98]:


# earliest date
df['Date'].min()


# In[99]:


# recent date
df['Date'].max()


# In[100]:


# we can subtract two dates in order to view the time between those dates and this is called TimeDelta.
df['Date'].max() - df['Date'].min()


# In[101]:


# data of 2020
filt = (df['Date'] >= '2020')
df.loc[filt]


# In[102]:


filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[filt]


# In[103]:


# another method to get all the 2019 data
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[filt]


# In[104]:


# set index as date and to change permanent we use inplace =True 
df.set_index('Date', inplace = True)


# In[105]:


df.loc['2019']


# In[106]:


df['2020-01':'2020-02']


# In[107]:


df['2020-01':'2020-02']['Close']


# In[108]:


df['2020-01':'2020-02']['Close'].mean()


# In[109]:


# high value for the day 
df['2020-01-01']['High'].max()


# In[110]:


# Resampling 
highs = df['High'].resample('D').max()
highs['2020-01-01']


# In[111]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[112]:


highs.plot()


# In[113]:


# resample on entire dataframe
df.resample('W').mean()


# In[114]:


# weekly overview
df.resample('W').agg({'Close':'mean','High':'max','Low':'min','Volume':'sum'})


# In[ ]:





# In[ ]:





# In[ ]:




