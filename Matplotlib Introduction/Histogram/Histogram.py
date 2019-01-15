#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.xlabel('Sugar Range')
plt.ylabel('Total Patient')
plt.title('Blood Sugar Analysis')
blood_sugar_man = [119,85,90,150,149,88,99,115,135,80,77,82,129]
blood_sugar_woman = [67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.hist([blood_sugar_man,blood_sugar_woman],bins=[80,100,125,150],rwidth=0.95 ,color=['green','orange'],label=['man','woman'])
plt.legend()


# In[ ]:




