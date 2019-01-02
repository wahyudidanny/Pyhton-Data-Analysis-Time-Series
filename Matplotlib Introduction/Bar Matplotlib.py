#!/usr/bin/env python
# coding: utf-8

# In[33]:


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Pyhton','Java','C++','C#','Perl','Scala') # kumpulan object array
# untuk membuat value Y , kita mengambil jumlah object array yang ada, 
y_pos = np.arange(len(objects)) # menjabarkan array berdasarkan jumlah object , ex: 5 maka 0,1,2,3,4
performance=[10,8,6,5,4,2] # Y value 

#mengset bar matplotlib bar
plt.bar(y_pos, performance, align='center', alpha=0.5) # mengset index array, value Y, align dan ketebalan
plt.xticks(y_pos,objects) # indentifikasi index X dari value objects
plt.ylabel('Usage') #label untuk Y
plt.xlabel('Programming Languages')#label untuk X
plt.show()
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.bar.html


# In[32]:


#jika mau membuat bar dengan horizontal maka hanya ganti function bar dengan barh, contoh

plt.barh(y_pos, performance, align='center', alpha=0.5) # mengset index array, value Y, align dan ketebalan
plt.yticks(y_pos,objects) # indentifikasi index Y dari value objects
plt.ylabel('Usage') #label untuk Y
plt.xlabel('Programming Languages')#label untuk X
plt.show()
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.barh.html


# In[48]:


#Bar dengan Group
#pertama set terlebih dahulu jumlah data yang akan digroup (n), ex: jumlah yang akan digroup = 5
import numpy as np
import matplotlib.pyplot as plt
 
n_group = 4
mean_satu = [90,55,35,20]
mean_dua = [20,40,55,49]

#rancang matplot
a,b = plt.subplots()
index = np.arange(n_group)

bar_width = 0.35 #panjang
bar_opacity = 0.8 #tebal

#set tiap bar
barsatu = plt.bar(index,mean_satu,bar_width,alpha=bar_opacity,color='g',label='Satu')
bardua = plt.bar(index + bar_width,mean_dua,bar_width,alpha=bar_opacity,color='b',label='Dua')
#bar dua dibuat berbeda dengan cara ditambah dengan widthnya, agar berdekatan jaraknya
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()
plt.tight_layout() # untuk mengatur otomatis antara subplot dengan subplot
plt.show()



# In[ ]:




