#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

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


# In[28]:


meanBBCAfirst = BBCA['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBCAlast = BBCA['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBCA  = float("%.2f" % (((meanBBCAlast - meanBBCAfirst)/meanBBCAfirst)* 100))
valuepersetanseBBCA, "%.2f" % meanBBCAfirst, "%.2f" %  meanBBCAlast
valuepersetanseBBCA


# In[29]:


meanBBNIfirst = BBNI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBNILast = BBNI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBNI = float("%.2f" % (((meanBBNIfirst - meanBBNILast)/meanBBNIfirst)* 100))
valuepersetanseBBNI, "%.2f" % meanBBNIfirst,"%.2f" % meanBBNILast
valuepersetanseBBNI


# In[30]:


meanBBRIfirst = BBRI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBRIlast = BBRI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBRI = float("%.2f" % (((meanBBRIfirst - meanBBRIlast)/meanBBRIfirst)* 100))
valuepersetanseBBRI, "%.2f" % meanBBRIfirst,meanBBRIlast
valuepersetanseBBRI


# In[31]:


meanBMRIfirst = BMRI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBMRIlast = BMRI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBMRI = float("%.2f" % (((meanBMRIfirst - meanBMRIlast)/meanBMRIfirst)* 100))
valuepersetanseBMRI, "%.2f" % meanBMRIfirst,"%.2f" % meanBMRIlast
valuepersetanseBMRI


# In[36]:


objects = ("BBCA","BBNI","BBRI","BMRI")
y_pos = np.arange(len(x)) # untuk mengeset array yang ada pada X
performance = [valuepersetanseBBCA, valuepersetanseBBNI, valuepersetanseBBRI, valuepersetanseBMRI]

plt.bar(y_pos,performance, align='center', alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Persentase') #label untuk Y
plt.xlabel('Stock Banking Indonesia')#label untuk X
plt.title('Persentase Kenaikan Harga Stock Banking Diindonesia 2018')
plt.show()

#sebelumnya tidak berjalan karena value dibuat menjadi string
#plt.title('Grafik Bar Persentase Kenaikan')
#plt.xlabel('Stock Finance Indonesia')
#plt.ylabel('Persentase Kenaikan')
#plt.bar(x, y, align='center', alpha=0.5)
#plt.show()


# In[ ]:





# In[ ]:




