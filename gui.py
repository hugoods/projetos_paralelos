# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:20:04 2020

@author: Hugo
"""
import random
import tkinter as tk
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
    if lista2 != []:    
        output_rows.append(sorted(lista2))
    else:
        None

janela = tk.Tk()
janela.geometry("280x100")
janela.title('Sorteio Mega-Sena')
janela.iconbitmap('D:/Users/Sony/Documents/MEGA-SENA/sorte.ico')

def sorteio():
    
    " essa funcao escolhe 6 numeros aleatorios e os organiza de forma crescente"
    nums = list(range(1, 61))
    random.shuffle(nums)
    six_nums = nums[:6]
    return sorted(six_nums)
def verificar():
    while sorteio() in output_rows:
        sorteio()
        break
    mylabel = tk.Label(janela, text=str(sorteio()))
    mylabel.pack()
    


botao = tk.Button(janela, text="Gerar sorteio", command=verificar)
botao.pack()

janela.mainloop()