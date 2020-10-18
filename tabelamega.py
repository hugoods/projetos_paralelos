# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:23:34 2020

@author: Hugo
"""

# importa BeautifulSoup


from bs4 import BeautifulSoup
import csv
html = open("h_mega.html").read()
soup = BeautifulSoup(html)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    lista = []
    for column in columns:
        output_row.append(column.integer.encode('utf-8'))
    lista.append(output_row[2:8])
    output_rows.append(lista)
    
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)