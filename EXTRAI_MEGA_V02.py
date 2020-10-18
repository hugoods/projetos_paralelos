import zipfile
import requests
from bs4 import BeautifulSoup
import openpyxl as px

url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
arquivo = requests.get(url)

open('D:/Users/Sony/Documents/MEGA-SENA/resultados.zip', 'wb').write(arquivo.content)

zip = zipfile.ZipFile('resultados.zip')

output_row = []
html = zip.read('d_megasc.htm')
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
last_row = table("tr")[-1]
columns = last_row.findAll('td')
for column in columns:
    output_row.append(column.text.encode('utf-8'))
print(output_row[2:8])

mega = px.load_workbook(filename = 'rainbow_v2.xlsx')
sort = mega.worksheets[0]
print(sort.max_row)