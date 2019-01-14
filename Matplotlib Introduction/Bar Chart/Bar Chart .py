#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
company = ['GOOGL','AMZN','MSFT','FB']
revenue = [90,136,89,27]
profit = [40,2,34,12]

xpos = np.arange(len(company))
plt.xticks(xpos,company)
plt.ylabel('revenue(bln)')
plt.title('US Tech Stocks')
plt.bar(xpos-0.2,revenue, width=0.4, label="Revenue")
plt.bar(xpos+0.2,profit, width=0.4, label="Profit")
plt.legend()


# In[5]:


plt.yticks(xpos,company)

plt.title('US Tech Stocks')
plt.barh(xpos-0.2,revenue, label="Revenue")
plt.barh(xpos+0.2,profit, label="Profit")
plt.legend()


# In[ ]:




