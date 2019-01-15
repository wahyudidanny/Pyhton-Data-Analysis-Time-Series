#!/usr/bin/env python
# coding: utf-8

# In[33]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

exp_values = [1600,600,300,420,250] 
exp_labels = ['Home Rent','Food','Phone/ Internet Bill','Car','Other Utilities'] 
plt.pie(exp_values,labels=exp_labels,radius=1.5,autopct='%0.1f%%',shadow=True,explode=[0,0.2,0,0,0],startangle=180)
plt.axis("equal")
plt.savefig('E:\\Github Repository\\Pyhton-Data-Analysis-Time-Series\\Matplotlib Introduction\\Pie Chart\\trysavepiechart.png',bbox_inches="tight",padinches="2",transparent=True)
plt.show()


# In[ ]:




