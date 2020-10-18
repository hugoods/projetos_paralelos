# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:13:52 2020

@author: Hugo
"""
import zipfile
import requests
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