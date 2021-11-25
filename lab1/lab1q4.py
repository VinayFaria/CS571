# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:34:34 2021

@author: vinay
"""

mat_rows = int(input().strip())
mat_columns = int(input().strip())

mat = []

for _ in range(mat_rows):
    mat.append(list(map(int, input().rstrip().split())))

squares = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        squares = squares + pow(mat[i][j],2)

sq_root = pow(squares,0.5)

Frobenius_Norm = round(sq_root,4)

print(Frobenius_Norm)