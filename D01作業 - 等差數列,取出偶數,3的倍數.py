#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[2]:


import numpy as np


# In[3]:


np.__version__


# In[ ]:


#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。

# In[60]:

a=np.arange(21)

# In[49]:

print(a)

# In[ ]:

#2.呈上題，將以上數列取出偶數。

# In[56]:

a[2:21:2]

# In[ ]:

#3.呈1題，將數列取出3的倍數。

# In[59]:

a[1:20:3]

