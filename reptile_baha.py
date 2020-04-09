#!/usr/bin/env python
# coding: utf-8

# In[77]:


import os
import shutil
dirname = 'pic'
path = '{}\\{}\\'.format(os.getcwd(),dirname)                  #os.getcwd() 可以取得現在位置
if not os.path.isdir(path):                             #若不存在
    os.mkdir(path) 


# In[78]:


import requests
from bs4 import BeautifulSoup as bs
res = requests.get (r'https://forum.gamer.com.tw/C.php?bsn=60076&snA=4320192')

soup = bs (res.text)
for img in soup.find_all("img", class_="lazyload"):
    if img['data-src'].find('.JPG') == -1:
        continue
    filename = img['data-src'].split('/')[-1]
    print (img['data-src'],img['data-src'].split('/')[-1])
    pic = requests.get(img['data-src'] ,stream=True)
    f = open ('{}\\{}'.format(path,filename),'wb')
    shutil.copyfileobj(pic.raw,f)
    f.close()