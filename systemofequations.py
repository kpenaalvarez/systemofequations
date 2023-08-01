# -*- coding: utf-
"""
Created on Mon Jul 31 17:17:44 2023

@author: kpenaalvarez
"""

import numpy as np
import sys

A = np.array([[2, -1, 3],
              [-1, 3, -1],
              [4, -4, 3]])

print(A)
type(A)
A.shape


'''
system of equations:
    suppose x1 = 5, and x2 + 1, then
    1*x1 + 2*x2 = 9
    3*1 + 4*2 v= 19
    
A@x = b
A.inv @ A.inv
'''

b = np.array([[10],
              [-1],
              [3]])
             
print(f"\nb = {b}")
        
             #solve questions
detA = np.linalg.det(A)
print(f"Determinant of matrix A is {detA: 0.3f}")
    
if detA == 0:
    print('\ndet A = 0; no solution\n')
    sys.exit()

        
Ainv = np.linalg.inv(A)
print(f"\nA-  inverse = \n{Ainv}")

print(f'\n Ainv @ A is {Ainv @ A}')

x = Ainv @ b

print(f"\nunknowns are: \n{x}")

#check
print(f"\ncheck: \n{A@x} ")