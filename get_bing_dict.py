#!/bin/python3
import requests as rq
import sys
from bs4 import BeautifulSoup

words = input() if len(sys.argv) <= 1 else ' '.join(sys.argv[1:])
url = 'https://cn.bing.com/dict/search'
r = rq.get(url, params={'q': words} )
soup = BeautifulSoup(r.text, 'lxml')

with open('/'.join(sys.argv[0].split('/')[:-1]) + '/style.css', 'r') as f:
    s = f.read()
soup.find_all('style')[0].string = s
#soup.html.body.header.decompose()
soup.html.body.footer.decompose()
soup.find_all(class_='sidebar')[0].decompose()

print(soup)


