# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:23:34 2020

@author: Hugo
"""

# importa BeautifulSoup

import random
from bs4 import BeautifulSoup

html = open("h_mega.html").read()
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    lista = []
    for column in columns:
        output_row.append(column.text.encode('utf-8'))
    lista.append(output_row[2:8])
    lista2 = []
    for l in lista[0]:
        lista2.append(int(l))
    output_rows.append(sorted(lista2))
   
def sorteio():
    " essa funcao escolhe 6 numeros aleatorios"
    nums = list(range(1, 61))
    random.shuffle(nums)
    six_nums = nums[:6]
    return sorted(six_nums)
while sorteio() in output_row:
    sorteio()
    break
print(sorteio())


