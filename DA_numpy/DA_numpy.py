#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#-----------------------------
# create a 1D array
#----------------------------
# ndarray
_array = np.array([10,20,30,40])
_array


# In[3]:


type(_array)


# In[4]:


# dtype   : int32,int64  : depending up the oS and python distribution
_array.dtype     


# In[5]:


# dimension of array
_array.ndim


# In[6]:


# size of array
_array.size


# In[7]:


# shape
_array.shape


# In[8]:


#-----------------------------
# create a 2D array
#----------------------------
_array2d = np.array([[10,20,30,40],[2,3,4,5]])
_array2d


# In[9]:


# dimension as 2
_array2d.ndim


# In[10]:


# shape   | 2 row and 4 columns
_array2d.shape


# In[11]:


# size should return 8 = 2 x 4 
_array2d.size


# In[12]:


# create 2d  3 x 3  array with all 0 
array0 = np.zeros((3,3))
array0


# In[13]:


# create 2d  4 x 4  array with all 1 
array1 = np.ones((4,4))
array1


# In[14]:


# create array from 10 to 20 
np.arange(10,21)


# In[15]:


# create array of all EVEN numbers from 10 to 20 
np.arange(10,21,2)


# In[16]:


# convert 1d array (of 0-15 ) into 2d array of 3x5
_array1 = np.arange(0,15)  
print(_array1)
_array12 = _array1.reshape(3,5)
print(_array12)

# in one line 
np.arange(0,15).reshape(3,5)


# In[17]:


#  linspace  |   splits the range into N number of interval
print(np.linspace(0,9,4) )   # N = 4
print(np.linspace(0,9,6) )   # N = 6


# In[18]:


# random 
print(np.random.random(5))

print(np.random.random((3,3)))


# In[19]:


# ==============================
# arithmetic operators
# ==============================
a1 = np.arange(5)
a1


# In[20]:


a1  + 5    # add 5 to each element


# In[21]:


# get 10 random numbers in between 1 - 50
np.random.random(10) * 50


# In[22]:


a1 = np.arange(21) / 2
a1


# In[23]:


#==============================
# Matric Product
# ==============================
A = np.arange(0, 9).reshape(3, 3)
B = np.ones((3, 3)) * 3
print("A:",A)
print("B:",B)


# In[24]:


A * B   # element wise multiplication  | NOTE : not matrix multiplication 


# In[25]:


np.dot(A,B)   # matrix multilication or DOT product      # there is no A . B   as . is not a arithmatic operator


# In[26]:


#==============================
# Aggregate functions 
#  a. sum 
#  b. min 
#  c. max 
#  d. mean
#  e. standard deviation
# ==============================

arr = np.array([11,22,3,55,34,23,20])
arr


# In[27]:


#  a. sum 
arr.sum()


# In[28]:


#  b. min 
arr.min()


# In[29]:


#  c. max
arr.max()


# In[30]:


arr.mean()


# In[31]:


arr.std()


# In[32]:


#==============================
# Indexing and slicing 
# ==============================

a = np.arange(10, 19)
a


# In[33]:


# 4th index | 5 the element as index starts from 0  
a[4]


# In[34]:


# last element of array
a[-1]


# In[35]:


# 3 rd element from last
a[-3]


# In[36]:


# splice |  2 to 5 th index
a[2:5]


# In[37]:


a[1:6:2]     # 1 to 6 th index 2 : alterate


# In[38]:


a[:6:2]    # start index 0 


# In[39]:


a[::2]    # same as a[0:9:2]


# In[40]:


a[::]


# In[41]:


# end 

