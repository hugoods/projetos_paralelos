# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:23:34 2020

@author: Hugo
"""

# importa BeautifulSoup
import zipfile
import requests
import random
from bs4 import BeautifulSoup

url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
arquivo = requests.get(url)

open('D:/Users/Sony/Documents/MEGA-SENA/teste.zip', 'wb').write(arquivo.content)

zip = zipfile.ZipFile('teste.zip')


html = zip.read('d_megasc.htm')
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr')[1:]:
    columns = table_row.findAll('td')
    output_row = []
    lista = []
    for column in columns:
        output_row.append(column.text.encode('utf-8'))
    lista.append(output_row[2:8])
    lista2 = []
    for l in lista[0]:
        lista2.append(int(l))
    if lista2 <> []:    
        output_rows.append(sorted(lista2))
    else:
        None
   
def sorteio():
    " essa funcao escolhe 6 numeros aleatorios e os organiza de forma crescente"
    nums = list(range(1, 61))
    random.shuffle(nums)
    six_nums = nums[:6]
    return sorted(six_nums)
while sorteio() in output_rows:
    sorteio()
    break
print(sorteio())


# for column in columns: