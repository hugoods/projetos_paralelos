# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:17:52 2020

@author: Hugo
"""

import openpyxl as px
arq = px.load_workbook(filename = u'rainbow_v2.xlsx')
pasta = arq.worksheets[2]
linhas = pasta.max_row + 1
gab = []
for l in range(3, linhas):
    lin = [int(pasta["C"+str(l)].value),
           int(pasta["D"+str(l)].value),
           int(pasta["E"+str(l)].value),
           int(pasta["F"+str(l)].value),
           int(pasta["G"+str(l)].value),
           int(pasta["H"+str(l)].value),]
    gab.append(lin)
    

print(gab)