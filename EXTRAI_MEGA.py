# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 17:50:06 2020

@author: Hugo
"""

import zipfile
import requests
from bs4 import BeautifulSoup
import openpyxl as px

url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
arquivo = requests.get(url)

open('D:/Users/Sony/Documents/MEGA-SENA/resultados.zip', 'wb').write(arquivo.content)

zip = zipfile.ZipFile('resultados.zip')


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
    if lista2 != []:    
        output_rows.append(sorted(lista2))
    else:
        None
        
mega = px.load_workbook(filename = 'rainbow_v2.xlsx')
sort = mega.worksheets[0]

for a in range(len(output_rows)):
    linha = a + 5
    sorteio = a + 1
    sort["A"+str(linha)] = sorteio
    sort["B"+str(linha)] = output_rows[a][0]
    sort["C"+str(linha)] = output_rows[a][1]
    sort["D"+str(linha)] = output_rows[a][2]
    sort["E"+str(linha)] = output_rows[a][3]
    sort["F"+str(linha)] = output_rows[a][4]
    sort["G"+str(linha)] = output_rows[a][5]

mega.save('rainbow_2284.xlsx')