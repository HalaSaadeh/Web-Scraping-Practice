import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url='http://www.dr-chuck.com/page1.htm'
html=urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #returns soup object

#Retrive all anchor tags
tags =soup('a')
for tag in tags:
    print(tag.get('href', None)) #get href key or none
