# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:56:45 2021

@author: vinay
"""

import csv

entries_dict = {}
infilename = 'result.txt'
file = open(infilename)
for line in file:
    num = line.strip()
    if str(num) in entries_dict.keys():
        entries_dict[str(num)] = entries_dict[str(num)] + int(num)
    else:
        entries_dict[str(num)] = int(num)

f = open('lab5q2_csvfile.csv', 'w', newline="")
writer = csv.writer(f)
for key,value in entries_dict.items():
    lst = [key,value]
    writer.writerow(lst)