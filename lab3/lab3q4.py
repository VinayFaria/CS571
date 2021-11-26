# -*- coding: utf-8 -*-

# for spyder
# @author: vinay

# function for returning string from 0 to 99
def n2w_h(n):
    try:
        return num2words[n]
    except KeyError:
        return num2words[n-n%10] + ' ' + num2words[n%10]

# function for returning string from 100 to 999
def n2w_t(n):
    dummy = n - (n//100)*100
    # if else loop for range checking 100 to 200 or 200 to 1000
    if n//100 == 0:
        return n2w_h(dummy)
    else: 
        return num2words[n//100] + ' hundred ' +n2w_h(dummy)

# function for checking number in which range it belongs to
def n2w(n):
    if n in range(0,100):
        print(n2w_h(n))
    elif n in range(100,1000):
        print(n2w_t(n))
    elif n in range(1000,10000):
        dummy = n - (n//1000)*1000
        print(num2words[n//1000] + ' thousand ' + n2w_t(dummy))
    else:
        print('Invalid input')
        
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero'}

number = int(input('Enter the number:'))
n2w(number)

"""
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numToWords' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER number as parameter.

# function for returning string from 0 to 99
def n2w_h(n):
    try:
        return num2words[n]
    except KeyError:
        return num2words[n-n%10] + ' ' + num2words[n%10]

# function for returning string from 100 to 999
def n2w_t(n):
    dummy = n - (n//100)*100
    # if else loop for range checking 100 to 200 or 200 to 1000
    if n//100 == 0:
        return n2w_h(dummy)
    else: 
        return num2words[n//100] + ' hundred ' +n2w_h(dummy)

# function for checking number in which range it belongs to
def n2w(n):
    if n in range(0,100):
        return n2w_h(n)
    elif n in range(100,1000):
        return n2w_t(n)
    elif n in range(1000,10000):
        dummy = n - (n//1000)*1000
        return num2words[n//1000] + ' thousand ' + n2w_t(dummy)
    else:
        return 'Invalid Input'
        
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero'}
            
def numToWords(number):
    # Write your code here
    return n2w(number)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number = int(input().strip())

    result = numToWords(number)

    fptr.write(result + '\n')

    fptr.close()

"""