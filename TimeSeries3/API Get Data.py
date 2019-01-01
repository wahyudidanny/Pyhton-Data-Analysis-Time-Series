#!/usr/bin/env python
# coding: utf-8

# In[70]:


import requests 

API_KEY = 'GWI8VYWKENVA8L11'
STOCKS = 'BBCA.jk'
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+STOCKS+'&apikey=' + API_KEY)

if (r.status_code == 200):
    result = r.json()
    dataForAllDays = result['Time Series (Daily)']
    dataForSingleDate = dataForAllDays['2018-12-31']['4. close']
    dataForSingleDate2 = dataForAllDays['2018-08-14']['4. close']

    #dataForSingleDate = dataForAllDays['2018-12-31']
    #dataForSingleDate = dataForAllDays['2018-12-31']
   # print (dataForAllDays)
    print (result)
    print (dataForSingleDate2)
   # print (dataForSingleDate['4. close'])
  #  print (datafirstDay['4. close'])
   # print (dataForSingleDate['1. open'])
   # print (dataForSingleDate['2. high'])
   # print (dataForSingleDate['3. low'])
   # print (dataForSingleDate['4. close'])
   # print (dataForSingleDate['5. volume'])
    
  


# In[ ]:




