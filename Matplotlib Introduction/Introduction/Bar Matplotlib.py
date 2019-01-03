#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x = [1,2,3,4,5,6,7]
y = [50,51,52,55,40,49,46]
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
plt.plot(x,y,color='green',linewidth=5,linestyle="dotted")


# In[ ]:




