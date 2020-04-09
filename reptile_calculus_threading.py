import requests
import urllib
import re
import _thread
from bs4 import BeautifulSoup as bs

def download(link, name):
        w = open("{}".format(name), "wb")
        data = urllib.request.urlopen(link).read()
        w.write(data)
        w.close()

fp = open("a.txt","w",encoding="utf-8")

url = "http://www.math.ntu.edu.tw/~hchu/Calculus/"
html = requests.get(url).text

sp = bs(html, "html.parser")

links = sp.find_all("a")

for link in links:
    href = link.get("href")
    if href != None and href.startswith("http://"):
        fp.write(href)
        fp.write("\n")
        name = re.sub("http://www.math.ntu.edu.tw/~hchu/Calculus/Calculus%5b104%5d-", "lecture", href)
        name = re.sub("http://www.math.ntu.edu.tw/~hchu/Calculus/AnsEx%5b", "answer", name)
        name = re.sub("%5d", "", name)
        _thread.start_new_thread(download,(href,name))

while 1:
    pass
         
print ("Main Finished")

# a = r"http://www.math.ntu.edu.tw/~hchu/Calculus/Calculus%5b104%5d-02.pdf"

# data = urllib.request.urlopen(a).read()
# w= open("b.pdf", "wb")
# w.write(data)