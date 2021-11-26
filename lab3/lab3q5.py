# -*- coding: utf-8 -*-
"""
@author: vinay
"""

def readandsum_input():
    ip = input('Enter number or press enter to add previous data:')
    # checking no input
    if ip == '':
        ip = 0
        return ip
    # checking if input entered is alphabet
    elif ip.isalpha():
        print('Enter number not alphabet')
        ip = 0
        return readandsum_input()
    # processing and looping back to take input
    else:
        ip = int(ip)
        return ip+readandsum_input()
    
sumofip = readandsum_input()
print(sumofip)