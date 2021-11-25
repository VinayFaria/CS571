# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:45:59 2021

@author: vinay
"""
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stackOperations' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY ops as parameter.
#
from collections import deque

def stackOperations(ops):
    # Write your code here
    final_list = []
    stack = []
    for string in ops:
        if string[0] == 'P':
            if len(stack) == 0:
                txt = string.split()
                word = txt[1]
                stack = deque([word])
            else:
                txt = string.split()
                word = txt[1]
                stack.append(word)
        elif string[0] == 'O':
            if len(stack) == 0:
                continue
            else:
                stack.pop()
        elif string[0] == 'M':
            txt = string.split()
            num = int(txt[1])
            for n_times_pop in range(num):
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
    if len(stack) == 0:
        string = 'EMPTY'
        final_list.append(string)
    else:
        for remaining_stack in range(len(stack)):
            if remaining_stack == (len(stack)-1):
                string = stack[len(stack)-1]+"*"
                final_list.append(string)
            else:
                string = stack[remaining_stack]
                final_list.append(string)
    return final_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ops_count = int(input().strip())

    ops = []

    for _ in range(ops_count):
        ops_item = input()
        ops.append(ops_item)

    result = stackOperations(ops)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
