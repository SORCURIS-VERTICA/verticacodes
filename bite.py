from bs4 import BeautifulSoup, SoupStrainer
import requests
import os

existfol = os.path.exists(".Loot")
if existfol == False:
    os.mkdir(".Loot")

def initialGet():
    url = input("LINK_BRO?::> ")
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data, features="html5lib")
    pracis(soup)

def pracis(soup):
    if os.path.exists("link2Get.txt"):
        os.remove("link2Get.txt")
    os.system("echo >> link2Get.txt")
    os.system("tsudo chmod +x link2Get.txt")
    f = open("link2Get.txt","a+")
    prevSab = None
    for link in soup.find_all('a'):
        curSab = link.get('href')
        if "4cdn" in curSab:
            curSab = curSab[2:]
            if curSab == prevSab:
                prevSab = curSab
            else:
                f.write(curSab)
                f.write("\n")
                prevSab = curSab
    f.close()
    os.system("wget -P .Loot -i link2Get.txt")
    
while True:
    initialGet()
