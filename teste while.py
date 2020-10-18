# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:37:47 2020

@author: Hugo
"""

import random
lista = [1, 2, 4, 5, 7]
dez06 = random.randint(1, 9)
print(dez06)
while dez06 in lista:
    dez06 = random.randint(1, 9)
    print(dez06)
    break
lista.append(dez06)