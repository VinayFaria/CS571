# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:32:02 2021

@author: vinay
"""

input_string = input('Enter the String:')
output = []
if input_string[0] == 'E':
    output_str = []
    output_count1 = []
    output_count2 = []
    
    stripped_string = input_string.lstrip('E')
    string_length = len(stripped_string)
    count = 0
    for i in range(string_length):
        if i == 0 or stripped_string[i] == stripped_string[i-1]:
            count = count + 1
        else:
            output_str.append(stripped_string[i-1])
            output_count1.append(count)
            count = 0
            count = count + 1
    output_str.append(stripped_string[i])
    output_count1.append(count)
    #print(output_count1)
    #print(output_str)
    for i in output_count1:
       output_count2 += str(i)
    #print(output_count2)
    for i in range(len(output_count2)):
        output.append(output_str[i])
        output.append(output_count2[i])
    str1 = ''.join(output)
    print(str1)
if input_string[0] == 'D':
    stripped_string = input_string.lstrip('D')
    string_length = len(stripped_string)
    count = 0
    for i in range(string_length):
        if stripped_string[i] == '0' or stripped_string[i] == '1' or stripped_string[i] == '2' or stripped_string[i] == '3' or stripped_string[i] == '4' or stripped_string[i] == '5' or stripped_string[i] == '6' or stripped_string[i] == '7' or stripped_string[i] == '8' or stripped_string[i] == '9':
            continue
        else:
            for j in range(int(stripped_string[i+1])):
                print(stripped_string[i])
    str1 = ''.join(output)
    print(str1)
        
        
        
        
        
        
"""    
    for i in range(string_length):
        if stripped_string[i] == 'a':
            count = count + 1
        elif stripped_string[i] == 'b':
            count = count + 1
        elif stripped_string[i] == 'c':
            count = count + 1
        elif stripped_string[i] == 'd':
            count = count + 1
        elif stripped_string[i] == 'e':
            count = count + 1
        elif stripped_string[i] == 'f':
            count = count + 1
        elif stripped_string[i] == 'g':
            count = count + 1
        elif stripped_string[i] == 'h':
            count = count + 1
        elif stripped_string[i] == 'i':
            count = count + 1
        elif stripped_string[i] == 'j':
            count = count + 1
        elif stripped_string[i] == 'k':
            count = count + 1
        elif stripped_string[i] == 'l':
            count = count + 1
        elif stripped_string[i] == 'm':
            count = count + 1
        elif stripped_string[i] == 'n':
            count = count + 1
        elif stripped_string[i] == 'o':
            count = count + 1
        elif stripped_string[i] == 'p':
            count = count + 1
        elif stripped_string[i] == 'q':
            count = count + 1
        elif stripped_string[i] == 'r':
            count = count + 1
        elif stripped_string[i] == 's':
            count = count + 1
        elif stripped_string[i] == 't':
            count = count + 1
        elif stripped_string[i] == 'u':
            count = count + 1
        elif stripped_string[i] == 'v':
            count = count + 1
        elif stripped_string[i] == 'w':
            count = count + 1
        elif stripped_string[i] == 'x':
            count = count + 1
        elif stripped_string[i] == 'y':
            count = count + 1
        elif stripped_string[i] == 'z':
            count = count + 1
elif input_string[0] == 'D':
    stripped_string = input_string.lstrip('D')
"""