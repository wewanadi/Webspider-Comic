# -*- coding: utf-8 -*-
#enter the comic number at https://www.cartoonmad.com/comic/[here].html to download
import requests
import urllib
import re
import _thread
import sys
from bs4 import BeautifulSoup as bs

# function for _thread to fork and download
def download (url,first_name,last_name):
    #print("start{}{}".format(first_name,last_name))
    #sys.stdout.flush()
    data = urllib.request.urlopen(url).read()
    w = open("One Punch/One Punch[{}_{}].jpg".format(int(first_name),last_name), "wb")
    w.write(data)
    w.close()
    print(first_name, last_name)
    sys.stdout.flush()

# get every part's url of the comic -> links
comic_num = 3583
url = "https://www.cartoonmad.com/comic/{}.html".format(str(comic_num))
html = requests.get(url).text
sp = bs(html, "html.parser")
links = sp.find_all("a")

for link in links:
    href = link.get("href")
    #print(href)
    if href != None and href.startswith("/comic/{}0".format(str(comic_num))):
        url = r'https://www.cartoonmad.com' + href
        html = requests.get(url).text
        sp = bs(html, "html.parser")
        pages = sp.find_all("a")
        max_page = 0

        # finding how much page this part have?
        for page in pages:
                if page.string != None and str(page).startswith('<a class="pages" href="{}0'.format(str(comic_num))):
                        if int(str(page.string)) > max_page:
                                max_page = int(str(page.string))
        
        # first name = which part of comic is
        tr = re.sub("https://www.cartoonmad.com/comic/{}0".format(str(comic_num)),"",url)
        first_name = tr[0]+tr[1]+tr[2]

        # download
        for i in range(1,max_page):
                last_name = "%03d" % i
                img_url = "https://www.cartoonmad.com/home75458/{}/{}/{}.jpg".format(comic_num,first_name,last_name)
                _thread.start_new_thread(download, (img_url, first_name, i))

while 1:
    pass

print("finish")
        
        