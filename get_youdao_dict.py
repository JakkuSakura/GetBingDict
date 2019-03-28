#!/bin/python3
import requests as rq
import sys
from bs4 import BeautifulSoup

words = input() if len(sys.argv) <= 1 else ' '.join(sys.argv[1:])
url = 'https://cn.bing.com/dict/search'
r = rq.get(url, params={'q': words} )
soup = BeautifulSoup(r.text, 'lxml')
style = soup.find_all('style')[0]
print(style)
content = soup.find_all(class_='lf_area')[0]
print(content)




