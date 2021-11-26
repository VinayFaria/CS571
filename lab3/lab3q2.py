#!/bin/python3

import os

#
# Complete the 'anacheck' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#Anagrams are words which should satisfy a) length of the words are equal b) number of times a alphabet in both words should be equal

def anacheck(str1, str2):
    # Write your code here
    elements1 = []
    elements2 = []
    for i in range(len(str1)):
        elements1.append(str1[i])
    for i in range(len(str2)):
        elements2.append(str2[i])
    
    if len(elements1) == len(elements2):
        elements1.sort()
        elements2.sort()
        if elements1 == elements2:
            boolean = True
        else:
            boolean = False
    else:
        boolean = False
    return boolean

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    str1 = input()

    str2 = input()

    result = anacheck(str1, str2)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
