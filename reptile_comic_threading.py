# -*- coding: utf-8 -*-
import requests
import urllib
import re,os
import threading
from bs4 import BeautifulSoup as bs
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def fork(url, first_name,last_name):
        data = urllib.request.urlopen(url).read()
        w = open("{}/{}[{}_{}].jpg".format(comic_name,comic_name,int(first_name),last_name), "wb")
        w.write(data)
        w.close()
        global now
        print("{}  [{}/{}] finished...".format(first_name, now, max_page))
        now += 1 

comic_num = 1633
comic_name = '山田和七個魔女'

path = '{}\\{}\\'.format(os.getcwd(),comic_name)
if not os.path.isdir(path):
    os.mkdir(path)

url = "https://www.cartoonmad.com/comic/{}.html".format(str(comic_num))
html = requests.get(url).text

sp = bs(html, "html.parser")

links = sp.find_all("a")
print("Strat Downloading from : [{}]".format(url))

for link in links:
    href = link.get("href")
    #print(href)
    if href != None and href.startswith("/comic/{}0".format(str(comic_num))):
        url = r'https://www.cartoonmad.com' + href
        html = requests.get(url).text
        sp = bs(html, "html.parser")
        pages = sp.find_all("a")
        max_page = 0
        for page in pages:
                if page.string != None and str(page).startswith('<a class="pages" href="{}0'.format(str(comic_num))):
                        if int(str(page.string)) > max_page:
                                max_page = int(str(page.string))
        tr = re.sub("https://www.cartoonmad.com/comic/{}0".format(str(comic_num)),"",url)
        first_name = tr[0]+tr[1]+tr[2]

        threads = []
        now = 1
        for i in range(1,max_page+1):
                last_name = "%03d" % i
                img_url = "https://www.cartoonmad.com/home75458/{}/{}/{}.jpg".format(comic_num,first_name,last_name)
                th = threading.Thread(target=fork, args=(img_url, first_name, i))
                th.start()
                threads.append(th)
        
        for thread in threads:
                thread.join()
        
print('Well Done！')

        
        