#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# In[8]:


meanBBCAfirst = BBCA['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBCAlast = BBCA['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBCA  = float("%.2f" % (((meanBBCAlast - meanBBCAfirst)/meanBBCAfirst)* 100))
valuepersetanseBBCA, "%.2f" % meanBBCAfirst, "%.2f" %  meanBBCAlast
valuepersetanseBBCA


# In[10]:


meanBBNIfirst = BBNI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBNILast = BBNI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBNI = float("%.2f" % (((meanBBNIfirst - meanBBNILast)/meanBBNIfirst)* 100))
valuepersetanseBBNI, "%.2f" % meanBBNIfirst,"%.2f" % meanBBNILast
valuepersetanseBBNI


# In[13]:


meanBBRIfirst = BBRI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBBRIlast = BBRI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBBRI = float("%.2f" % (((meanBBRIfirst - meanBBRIlast)/meanBBRIfirst)* 100))
valuepersetanseBBRI, "%.2f" % meanBBRIfirst,meanBBRIlast
valuepersetanseBBRI


# In[12]:


meanBMRIfirst = BMRI['2018-01-01':"2018-01-31"].dropna(how='all').Close.mean()
meanBMRIlast = BMRI['2018-11-01':"2018-11-30"].dropna(how='all').Close.mean()
valuepersetanseBMRI = float("%.2f" % (((meanBMRIfirst - meanBMRIlast)/meanBMRIfirst)* 100))
valuepersetanseBMRI, "%.2f" % meanBMRIfirst,"%.2f" % meanBMRIlast
valuepersetanseBMRI


# In[14]:


objects = ("BBCA","BBNI","BBRI","BMRI")
y_pos = np.arange(len(objects)) # untuk mengeset array yang ada pada X
performance = [valuepersetanseBBCA, valuepersetanseBBNI, valuepersetanseBBRI, valuepersetanseBMRI]
plt.bar(y_pos,performance, align='center', alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel('Persentase') #label untuk Y
plt.xlabel('Stock Banking Indonesia')#label untuk X
plt.title('Persentase Kenaikan Harga Stock Banking Diindonesia 2018')
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()


# In[25]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

N = 5
men_means = (54.74, 42.35, 67.37, 58.24, 30.25)
men_std= (4, 3, 4, 1, 5)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)

# add some text for labels, title and axes ticks
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')

red_patch = mpatches.Patch(color='red', label='Men')
plt.legend(handles=[red_patch])


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
       height = rect.get_height()
       ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
       ha='center', va='bottom')
autolabel(rects1)
plt.show()


# In[ ]:




