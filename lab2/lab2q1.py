#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sparseMatOps' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY sm_a
#  2. INTEGER_ARRAY sm_b
#  3. STRING_ARRAY ops
#

from collections import Counter
# Skeleton for sparse matrix operations

# add two sparse matrices
def smAdd(sm_ad,sm_bd):
    #Adds two compatible sparse matrices.
    dummy = sm_ad.copy()
    for key,value in sm_bd.items():
        dummy[key] = value
    for i in dummy:
        sm_ad[i] = sm_ad.get(i,0) + sm_bd.get(i,0)
    return sm_ad

def smSub(sm_ad,sm_bd):
    #Adds two compatible sparse matrices.
    dummy = sm_ad.copy()
    for key,value in sm_bd.items():
        dummy[key] = value
    for i in dummy:
        sm_ad[i] = sm_ad.get(i,0) - sm_bd.get(i,0)
    return sm_ad

def smRSub(sm_ad,sm_bd):
    #Adds two compatible sparse matrices.
    dummy = sm_ad.copy()
    for key,value in sm_bd.items():
        dummy[key] = value
    for i in dummy:
        sm_ad[i] = sm_bd.get(i,0) - sm_ad.get(i,0)
    return sm_ad

def smScale(sm_ad,k):
    #Scales a sparse matrix.
    for i in sm_ad:
        sm_ad[i] = sm_ad[i]*k
    return sm_ad

def sparseMatOps(sm_a, sm_b, ops):
    # Write your code here
    sm_ad = {}
    sm_bd = {}
    row = 0
    column = 0
    # Input the SM sm_a and sm_b
    # You can either hard-code it here, or,
    # read from a file, or,
    # ask the user to input the values (tedious!)
    # Remember to ask for the dimensions of the matrices first.
    # Form the dictionaries representing sm_a, sm_b
    for i in range(sm_a[2]):
        count = 3*(i+1)
        sm_ad[(sm_a[count],sm_a[count+1])] = sm_a[count+2]
    
    for i in range(sm_b[2]):
        count = 3*(i+1)
        sm_bd[(sm_b[count],sm_b[count+1])] = sm_b[count+2]
        
    row = sm_a[0]
    column = sm_a[1]
        
    for i in range(len(ops)):
        if ops[i] == 'A':        
            # Perform addition
            # First check if dimensions are compatible for addition
            # If yes, then proceed.
            if sm_a[0] == sm_b[0] and sm_a[1] == sm_b[1]:
                sm_ad = smAdd(sm_ad,sm_bd)
            # Display the result
            #smPrint(sm_c)

        if ops[i] == 'S':        
            # Perform Subtraction
            # First check if dimensions are compatible for Subtraction
            # If yes, then proceed.
            if sm_a[0] == sm_b[0] and sm_a[1] == sm_b[1]:
                sm_ad = smSub(sm_ad,sm_bd)
            # Display the result
            #smPrint(sm_c)
        
        if ops[i] == 'R':        
            # Perform Reverse Subtraction
            # First check if dimensions are compatible for Reverse Subtraction
            # If yes, then proceed.
            if sm_a[0] == sm_b[0] and sm_a[1] == sm_b[1]:
                sm_ad = smRSub(sm_ad,sm_bd)
            # Display the result
            #smPrint(sm_c)

        if ops[i][0] == 'C':
            txt = ops[i].split()
            k = int(txt[1])
            # perform scaling
            # get the input k
            sm_ad = smScale(sm_ad,k)
            # Display the result
            #smPrint(sm_d)

    sm_a.clear()
    sm_a.append(row)
    sm_a.append(column)
    sm_a.append(len(sm_ad))
    count = 3
    for i in sorted(sm_ad.keys()):
        sm_a.append(i[0])
        sm_a.append(i[1])
        sm_a.append(sm_ad[i])
        count += 3
    return sm_a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sm_a_count = int(input().strip())

    sm_a = []

    for _ in range(sm_a_count):
        sm_a_item = int(input().strip())
        sm_a.append(sm_a_item)

    sm_b_count = int(input().strip())

    sm_b = []

    for _ in range(sm_b_count):
        sm_b_item = int(input().strip())
        sm_b.append(sm_b_item)

    ops_count = int(input().strip())

    ops = []

    for _ in range(ops_count):
        ops_item = input()
        ops.append(ops_item)

    result = sparseMatOps(sm_a, sm_b, ops)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
