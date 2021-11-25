# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:48:25 2021

@author: vinay
"""

element = []
n = int(input('Enter number of elements you want in list:'))

for i in range(n):
    temp = int(input())
    element.append(temp)
    
single_elements_list = set(element)
print(single_elements_list)

sorted_elements = sorted(single_elements_list)

#for j in range(len(single_elements_list)):
count = []
for j in sorted_elements:
    count.append(j)
    count.append(element.count(j))
print(count)

"""
counting = dict()

for i in range(len(sorted_elements)):
    counting.update(sorted_elements[i])

print(counting)
"""    