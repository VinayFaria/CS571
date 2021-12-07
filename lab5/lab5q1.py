# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:03:06 2021

@author: vinay
"""
import csv
department = {}
department_city = {}
dummy = []
infilename = 'data_records.txt'
file = open(infilename)
for line in file:
    dummy = line.split()
    if dummy[5] in department:
        department[dummy[5]] += 1
    else:
        department[dummy[5]] = 1

print('\n'.join(['The department "{0}" contain {1} number of employee'.format(k, v) for k,v in department.items()]))
file.close()
print('\n')
file = open(infilename)
for line in file:
    dummy = line.split()
    if (dummy[5],dummy[4]) in department_city:
        department_city[dummy[5],dummy[4]] += 1
    else:
        department_city[dummy[5],dummy[4]] = 1

print('\n'.join(['The department "{0}" contain {1} number of employee from {2} city'.format(k[0], v, k[1]) for k,v in department_city.items()]))
file.close()
print('\n')
file = open(infilename)
f = open('lab5q1_csvfile.csv', 'w', newline="")
writer = csv.writer(f)
for line in file:
    dummy = line.split()
    lst = [dummy[1] + ' ' + dummy[2], dummy[4]]
    writer.writerow(lst)

file.close()
f.close()