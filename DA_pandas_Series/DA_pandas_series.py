#!/usr/bin/env python
# coding: utf-8

# In[1]:


#------------------------------------------
# install pandas
#------------------------------------------
# pip install pandas
# sudo apt-get install python-pandas
# conda instal pandas

#------------------------------------------
# import section
#------------------------------------------
import pandas as pd
import numpy as np
# from pandas import *
#=========================================================
#  Pandas Datastructure | Series
#=========================================================


# In[2]:


#------------------------------------------
# 1. declaring a series
#-------------------------------------------

# here default index = 0 ,1,2 ...

_series = pd.Series([1,4,-7,22,34,67,53])
_series
# series = pd.Series(np.array([1,4,-7,22,34,67,53]))   # define by np.array


# In[3]:


# explicity index
_series = pd.Series([1,4,-7,22,34,67,53],index=['a','b','c','d','e','f','g'])
_series


# In[4]:


# indexes and values
_series.index


# In[5]:


_series.values


# In[6]:


#------------------------------------------
# 2. Selecting the internal elements
#-------------------------------------------
# by index
_series['c']


# In[7]:


# by key 
_series[2]


# In[8]:


# multiple elements as in numpy  | by key range
_series[1:4]


# In[9]:


# multiple elements | by index list
_series[['b','d']]


# In[10]:


#------------------------------------------
# 3. Assigning values to the elements
#-------------------------------------------
# by key
_series[2] = -222
_series


# In[11]:


# by index
_series['f'] = 234345
_series


# In[12]:


#------------------------------------------
# 4. Filtering values
#-------------------------------------------
_series[_series > 100]


# In[13]:


#_series[_series == 4 ] # 
_series[_series != 4 ] # not equal 4


# In[14]:


#------------------------------------------
# 5. Operations
#-------------------------------------------
# +,-,* % , / 
_series + 100  # add 100 to each element


# In[15]:


# module of 2
_series % 2  # odd(1) or even(0) 


# In[16]:


# log of all elements 
np.log(_series)
# np.sin , 


# In[17]:


np.sin(_series)   # sin,exp


# In[18]:


# uniqe elements
s1 = pd.Series([1,22,22,44,55,7,44,np.NaN])   # NaN : Not a NUmber   1/0
s1.unique() # uniq elements in  


# In[19]:


# check if certain element(s) is present or not
s1.isin([1,7])


# In[20]:


s1.isin([1,7]).values


# In[21]:


s1.isin([1,7]).value_counts()


# In[22]:


# check if any NUll number is present
s1.isnull()


# In[23]:


s1.notnull()


# In[24]:


# get the Null and Not Null COunts series
s1.notnull().value_counts()

# s1.notnull().value_counts()[True]
# s1.notnull().value_counts()[False]


# In[25]:


# filter all not NULL elements
s1[s1.notnull()]


# In[26]:


# filter all NaN 
# s1.isnull().value_counts()[True]   # count
s1[s1.isnull()]


# In[27]:


#------------------------------------------
# 6. Series as Dictionaries
#-------------------------------------------
mydict = {'red': 20, 'blue': 10, 'yellow': 50,'orange': 70}
mydict


# In[28]:


myseries = pd.Series(mydict)
myseries


# In[29]:


#------------------------------------------
# 7. Operation betweeb Series
#-------------------------------------------
s1 = pd.Series([11,22,33,44,55],index=['a','b','c','d','e'])
s1


# In[30]:


s2 = pd.Series({'a':111,'bb':222,'c':333})
s2


# In[31]:


s1 + s2


# In[ ]:





# In[32]:


# thank you 
# stay tuned for upcoming topics

