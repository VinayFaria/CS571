#!/bin/python3

import os

#
# Complete the 'uniqueChars' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING inputStr as parameter.
#

def uniqueChars(inputStr):
    # Write your code here
    elements = []
    single_elements = []
    for i in range(len(inputStr)):
        elements.append(inputStr[i])
        
    for i in elements:
        if i in single_elements:
            continue
        else:
            single_elements.append(i)
    return len(single_elements)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputStr = input()

    result = uniqueChars(inputStr)

    fptr.write(str(result) + '\n')

    fptr.close()
