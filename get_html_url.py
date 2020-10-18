# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:44:46 2020

@author: Hugo
"""

import requests
from bs4 import BeautifulSoup

url = "https://lotorainbow.com.br/po/probteorica.asp?pag=1&idloto=2&orig=P&tpvis=T"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

match = soup.find('td', class_='')
print(match)