#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df1 = pd.DataFrame({'C':[80,85,88,85],
                    'C12':[2, 3, 2, 2],
                    'C13':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])
print(df1)


# In[7]:



df2 = pd.DataFrame({'C':[80,85,88,85],
                    'C22':[2, 3, 2, 2],
                    'C23':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])
print(df2)


# In[8]:


df3 = pd.DataFrame({'C':[80,85,88,85],
                    'C32':[7, 8, 9, 6],
                    'C33':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
print(df3)


# In[5]:


print(pd.merge(df1,df3, on='C'))


# In[ ]:




