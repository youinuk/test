# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:38:36 2021

@author: Inuk You
"""

import sys

n = 1000
j = n/2
low = 0
high = n
for i in range(1, n+1):
    print(i, 'th: is it', j, '?')
    sys.stdout.flush()
    reply = input()
    if reply == 'CORRECT':
        break
    elif reply == 'UP':
        low = j
    elif reply == 'DOWN':
        high = j
    j = int((low + high)/2)