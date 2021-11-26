# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:15:50 2021

@author: vinay
"""
pascal_list = []
num_of_rows = int(input('Enter input:'))
dummy1 = []
#pascal triangle using for loop
for i in range(num_of_rows):
    for j in range(i+1):
        # checking if 1st or last elements then its value should be 1
        if j == 0 or j == (len(range(i+1)) - 1):
            dummy1.append(1)
        else:
            # adding previous row elements
            dummy1.append(pascal_list[i-1][j-1]+pascal_list[i-1][j])
    # making a copy in dummy2 so that when dummy1 is clear pascal_list is not cleared
    dummy2 = dummy1.copy()
    # appending dummy2 to pascal_list for every row
    pascal_list.append(dummy2)
    dummy1.clear()

print(pascal_list)