#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


#========================================
# read  : CSV and TXT file
#========================================
csvfile = "vehicle_data.csv"   # current dir 

# now read 
csvdf = pd.read_csv(csvfile)
csvdf


# In[3]:


# no header
pd.read_csv(csvfile,header=None)
pd.read_csv(csvfile,names=['col0','col1','col2','col3','col4','col5'])


# In[4]:


# hierarchical structure
pd.read_csv(csvfile,index_col=['city','vehicle'])


# In[5]:


# read portion of the file 
# ,header=None
pd.read_csv(csvfile,skiprows=[2,4],nrows=6)
#pd.read_csv(csvfile,skiprows=2,nrows=6)


# In[6]:


#========================================
# read  : TXT file
#========================================
logdf = pd.read_table('txt_samplelog.txt')
logdf


# In[7]:


logdf = pd.read_table('txt_samplelog.txt',sep=',',skiprows=[0,1,3,7])
logdf


# In[8]:


# ---------------------------------------------
# parse TXT file using RegExp 
# ---------------------------------------------
#  .    Single character, except newline
# \d    Digit
# \D    Non-digit character
# \s    Whitespace character
# \S    Non-whitespace character
# \n    New line character
# \t    Tab character

#pd.read_table('samplelog.txt',sep='\s',engine='python')


# In[9]:


# ---------------------------------------------
# Write to CSV FILE
# ---------------------------------------------
_csvdf = csvdf.sample(6)  # head , tail , sample
_csvdf


# In[10]:


# Write to outfile.csv
_csvdf.to_csv("csv_outfile.csv")

_csvdf.to_csv("csv_outfile_noheader_noindex.csv",index=False,header=False)


# In[11]:


#========================================
# read / write  : HTML file
#========================================
print(_csvdf.to_html())   # to html string


# In[12]:


# to html file
_html  = '<html><head><title>Dataframe dump to html</title></head><body>'
_html += _csvdf.to_html()
_html += '</body></html>'
htmlfile = open('html_outfile.html','w')
htmlfile.write(_html)
htmlfile.close()


# In[13]:


# read data from html file
htmldf = pd.read_html('html_read.html')
htmldf


# In[14]:


htmldf[1]


# In[15]:


#========================================
# read / write  : EXCEL file
#========================================


# In[16]:


cardf = pd.read_excel('xls_vehicle.xlsx')


# In[17]:


pd.read_excel('xls_vehicle.xlsx','Bikes')  # select the SheetName


# In[18]:


bikedf = pd.read_excel('xls_vehicle.xlsx',1) # select the Sheet Index


# In[19]:


# write to excel
cardf.to_excel('xls_outfile.xlsx',sheet_name='NewCars')
bikedf.to_excel('xls_outfile.xlsx',sheet_name='NewBikes')


# In[20]:


# write multiple sheets in a single Excel file
with pd.ExcelWriter('xls_outfile_all.xlsx') as xls:
    cardf.to_excel(xls,sheet_name='NewCars')
    bikedf.to_excel(xls,sheet_name='NewBikes')


# In[21]:


#========================================
# read  : XML file
#========================================
from lxml import objectify
import xml.etree.ElementTree as ET
import xml.dom.minidom


xmlobj = objectify.parse('xml_book.xml')
xmlobj

root = xmlobj.getroot()
print(root.Book.Author)
print(root.getchildren())


# In[22]:


#========================================
# read/write  : JSON file
#========================================
# write
bikedf.to_json('json_bikes.json')


# In[23]:


# read json
newbikedf = pd.read_json('json_bikes.json')
newbikedf


# In[24]:


"""
import json
from pandas.io.json import json_normalize
jsonfile = open('json_bikes.json','r')
lines = jsonfile.read()
lines  = json.loads(lines)
lines
json_normalize(lines)
"""


# In[25]:


#========================================
# read/write  : Python Pickle file
#========================================
import pickle
data = { 'color': ['white','red'], 'value': [5, 7]}


# In[26]:


pickled_data = pickle.dumps(data)   # serialize/write to pickle 
print(type(pickled_data))
pickled_data


# In[27]:


_data = pickle.loads(pickled_data)  # deserialize / read from a pickle
print(type(_data))
_data


# In[28]:


# with panda dataframe
bikedf.to_pickle('pickle_bikes.pkl')  # write


# In[29]:


# after some months u can eat the pickle

_newbikedf = pd.read_pickle('pickle_bikes.pkl') # read 
_newbikedf


# In[30]:


# Thanks you for watching 

