# -*- coding: utf-8 -*-

# for spyder
# @author: vinay
def gcd_process(dummy):
    if dummy[0] == 0:
        #since GCD(0,B) = B
        return dummy[1]
    elif dummy[1] == 0:
        #since GCD(A,0) = A
        return dummy[0]
    else:
        #In GCD(A,B),for A>B, A=B*quotient+remainder
        remainder = dummy[0]%dummy[1]
        dummy[0] = dummy[1]
        dummy[1] = remainder
        dummy.sort(reverse=True)
        return gcd_process(dummy)
        
a = int(input('Enter the 1st number:'))
b = int(input('Enter the 2nd number:'))
gcd_of_a_and_b = [a,b]
gcdnum_sorted = sorted(gcd_of_a_and_b, reverse=True)  #making 2 number in descending order
gcd_output = gcd_process(gcdnum_sorted)
print(gcd_output)

"""
# for hackerrank
# @author: vinay

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'euclidGCD' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
def gcd_process(dummy):
    if dummy[0] == 0:
        #since GCD(0,B) = B
        return dummy[1]
    elif dummy[1] == 0:
        #since GCD(A,0) = A
        return dummy[0]
    else:
        #In GCD(A,B),for A>B, A=B*quotient+remainder
        remainder = dummy[0]%dummy[1]
        dummy[0] = dummy[1]
        dummy[1] = remainder
        dummy.sort(reverse=True)
        return gcd_process(dummy)
    
def euclidGCD(a, b):
    # Write your code here
    gcd_of_a_and_b = [a,b]
    gcdnum_sorted = sorted(gcd_of_a_and_b, reverse=True)  #making 2 number in descending order
    gcd_output = gcd_process(gcdnum_sorted)
    return gcd_output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    b = int(input().strip())

    result = euclidGCD(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()

"""