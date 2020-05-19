#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


np.zeros(10, dtype=int)


# In[4]:


L=np.zeros(10, dtype=float)


# In[3]:


np.zeros(10, dtype='<U1') #or str


# In[6]:


[str(c) for c in L]


# In[7]:


np.arange(10)


# In[8]:


np.array(range(10))


# In[9]:


np.linspace(1,2,4)


# In[10]:


np.random.normal(0,5,(4,5))


# In[11]:


np.random.poisson(8,(4,5))


# In[12]:


np.random.poisson(8,(4,5))


# In[13]:


x1 = np.random.randint(100, size=6)
x2 = np.random.randint(10, size=(3,4)) #two dimension
x3 = np.random.randint(10, size=(3,4,5))


# In[14]:


x1,
x2,
x3


# In[15]:


x1


# In[16]:


x2


# In[17]:


x3


# In[18]:


np.random.random(6)


# In[19]:


x=[1,2]+list(range(10))


# In[20]:


x


# In[21]:


x[11::-1]


# In[29]:



np.concatenate([[1,2],[3]])


# In[30]:


grid = np.array([[1,2,3],[4,5,6]])
np.concatenate([grid,grid])


# In[38]:


grid = np.array([[1,2,3],[4,5,6]])
np.concatenate([x3,x3],axis=2)


# In[41]:


x = np.array([3,4,5])
grid = np.array([[1,2,3],[17,18,19]])
np.vstack([x,grid])
#vertical stack


# In[40]:


z = np.array([[9],[9]])
np.hstack([grid,z])
#horizontal stack


# In[42]:


import pandas as pd


# In[44]:


x0=np.arange(10)
x1,x2,x3 = np.split(x0,[3,6])
print (x1,x2,x3)


# In[46]:


grid = np.arange(16).reshape((8,2))
grid


# In[47]:


upper,lower = np.vsplit(grid,[2])
print (upper, lower)


# In[ ]:




