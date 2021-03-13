#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# supress wrarning 
#import warnings
#warnings.filterwarnings('ignore')


# In[4]:


data = {
    'color' : ['green','blue','yellow','red','orange'],
    'items' : ['grass','sky','pen','signal','fruit'],
    'rating' : [1,2,3,3,5],
    'price' : [1,2.2,44,55.25,99]
 }
# dataframe 
df = pd.DataFrame(data)
df


# In[7]:


# create dataframe with specific columns
df1 = pd.DataFrame(data,columns=['items','price'])
df1


# In[8]:


# change the default index (similar to Series)
df2 = pd.DataFrame(data,index=['one','two','three','four','five'])
df2


# In[9]:


# instead of using data from dict object, 
# we do so by 3 arguments : matrix data, index , columns
data3 = np.arange(16).reshape((4,4))
data3 


# In[142]:


df3 = pd.DataFrame(
    data3, 
    index = ['one','two','three','four'],
    columns = ['colors','items','rating','price']
)
df3


# In[11]:


# ----------------------------------------
# 1. selecting elements
#----------------------------------------
# get columns
df.columns


# In[12]:


# list of index
df.index


# In[16]:


# values
df.values


# In[17]:


# content of a column
df['color']      # or df.price


# In[19]:


df.loc[1]


# In[20]:


df.loc[1:3]   # range from 1 to 3


# In[21]:


df.loc[[2,4]]   # 2nd and 4th


# In[22]:


# get the 2nd index color name
df['color'][2]     # column name and index


# In[ ]:


df.color[2]  # attribute and index


# In[24]:


df.loc[2]['color']


# In[28]:


df.loc[2].color


# In[108]:


df.loc[2,'color']    # we will use it quite often 


# In[31]:


# ----------------------------------------
# 2. Assigning values elements
#----------------------------------------
df.index.name  = 'rowid'
df.columns.name = 'colnames'
df


# In[35]:


# add new column with their value
df['newcol'] = 'new value'
df


# In[56]:


df['newcol'] = [1,3,2,41,4]  # or pd.Series(np.arange(5))   
df['newcol'] = pd.Series(np.arange(5))
df['newcol'] = pd.Series(np.random.randn(5))  # 5 random number
df


# In[107]:


# for changing a price of yellow pen to new value INR ?
df['price'][2] = 1234 
df.loc[2,'price'] = 8881   
df


# In[109]:


# ----------------------------------------
# 3. membership of a value
#----------------------------------------
# we have already seen isin()   in Series
df.isin([2.2,'price'])


# In[110]:


# new data frame containing only the values that satisfy the condition
df[df.isin([2.2,'price'])]


# In[113]:


# ----------------------------------------
# 4. Deleting a column
# ----------------------------------------
del df['newcol']
df


# In[120]:


df['newcol1'] = pd.Series(np.random.randn(5))

newdf = df.drop(columns=['newcol1'])   # drop doesnt delete from the original df
newdf
#df


# In[124]:


# ----------------------------------------
# 5. Filtering
# ----------------------------------------
# filter all values : rows and columns
df[df < 10]


# In[123]:


# filter with a column data
df[df.price < 10]


# In[125]:


df[df.color == 'red']


# In[132]:


# filter with multiple conditions 
df[( df.rating == 3 ) & (df.color == 'red')]
#df[df.rating.isin([1,2])] 


# In[134]:


# ----------------------------------------
# 6. DataFrame from Nested Dict
# ----------------------------------------

_nestdict = { 
     'red': {2012:11,2020:22, 2013: 33 },
     'white': { 2011: 13, 2012: 22, 2013: 16},
     'yellow': {2021: 17, 2012: 334, 2013: 22},
     'blue': {2011: 17, 2012: 27, 2013: 18}
}
df1 = pd.DataFrame(_nestdict)
df1


# In[135]:


# ----------------------------------------
# 7. Transposition of a DataFrame
# ----------------------------------------
# column -> rows  and rows -> columns
df1.T


# In[139]:


# ----------------------------------------
# 8. Arithmetic methods 
# ----------------------------------------
# add()
# sub()
# div()
# mult()
# ----------------------------------------
df11 =  pd.DataFrame(
    np.arange(25).reshape((5,5)),
    index=['red','blue','yellow','white','green'],
    columns=['ball','pen','pencil','paper','ipad']
)
df11


# In[140]:


df22 = pd.DataFrame(
    np.arange(15).reshape((5,3)),
    index=['blue','green','white','yellow','cyan'],
    columns=['mug','pen','ball']
)
df22


# In[143]:


df11 + df22


# In[144]:


df11.add(df22)


# In[145]:


#------------------------------------
# functions by element : each value in the dataframe
#------------------------------------
# np.sqrt , exp , sin , log ..
np.sqrt(df11)


# In[161]:


# ------------------------------------
# functions by  : rows or column
# ------------------------------------
# sum , mean , max , min 
df11.max()


# In[157]:


np.max(df11)


# In[158]:


def band(rec):   
    """
    band = max - min of the column
    """
    return rec.max() - rec.min()


#band(df11)
df11.apply(band)   # columns wise max - min


# In[159]:


# row wise : band : max - min
df11.apply(band,axis=1) 


# In[160]:


df11


# In[162]:


df11.describe()


# In[ ]:


# thank you  :) 
# stay tuned for upcoming topics

