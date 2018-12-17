#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

BBCA = pd.read_csv('E:\Github Repository\Pyhton-Data-Analysis-Time-Series\TimeSeries3\File CSV\BBCA.JK.csv',parse_dates=["Date"],index_col="Date")
BBNI = pd.read_csv('E:\Github Repository\Pyhton-Data-Analysis-Time-Series\TimeSeries3\File CSV\BBNI.JK.csv',parse_dates=["Date"],index_col="Date")
BBRI = pd.read_csv('E:\Github Repository\Pyhton-Data-Analysis-Time-Series\TimeSeries3\File CSV\BBRI.JK.csv',parse_dates=["Date"],index_col="Date")
BMRI = pd.read_csv('E:\Github Repository\Pyhton-Data-Analysis-Time-Series\TimeSeries3\File CSV\BMRI.JK.csv',parse_dates=["Date"],index_col="Date")
BBCA['2018-01-01':"2018-12-17"].dropna(how='all').Close.plot() 
BBNI['2018-01-01':"2018-12-17"].dropna(how='all').Close.plot() 
BBRI['2018-01-01':"2018-12-17"].dropna(how='all').Close.plot() 
BMRI['2018-01-01':"2018-12-17"].dropna(how='all').Close.plot()
plt.legend(["BBCA","BBNI","BBRI","BMRI"]) 
plt.title("4 Banking Stock Indonesia") #to create a title
plt.xlabel("Year 2018") #to create label in x
plt.ylabel("Price") #to create label in x

#plt.plot(dfBBCA,dfBBNI)


# In[53]:


meanBBCAfirst = BBCA['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBCAlast = BBCA['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBCA  = "%.2f" % (((meanBBCAlast - meanBBCAfirst)/meanBBCAfirst)* 100)
valuepersetanseBBCA, "%.2f" % meanBBCAfirst, "%.2f" %  meanBBCAlast


# In[55]:


meanBBNIfirst = BBNI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBNILast = BBNI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBNI = "%.2f" % (((meanBBNIfirst - meanBBNILast)/meanBBNIfirst)* 100)
valuepersetanseBBNI, "%.2f" % meanBBNIfirst,"%.2f" % meanBBNILast


# In[56]:


meanBBRIfirst = BBRI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBRIlast = BBRI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBRI = "%.2f" % (((meanBBRIfirst - meanBBRIlast)/meanBBRIfirst)* 100)
valuepersetanseBBRI, "%.2f" % meanBBRIfirst,meanBBRIlast


# In[57]:


meanBMRIfirst = BMRI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBMRIlast = BMRI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBMRI = "%.2f" % (((meanBMRIfirst - meanBMRIlast)/meanBMRIfirst)* 100)
valuepersetanseBMRI, "%.2f" % meanBMRIfirst,"%.2f" % meanBMRIlast


# In[77]:


x = np.array(["BBCA","BBNI","BBRI","BMRI"])
y = [5, 10, 15, 20]
plt.title('Grafik Bar Persentase Kenaikan')
plt.xlabel('Stock Finance Indonesia')
plt.ylabel('Persentase Kenaikan')
plt.bar(x, y, align='center', alpha=0.5)
plt.show()


# In[ ]:




