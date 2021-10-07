# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:12:34 2021

GIVENS METHOD
@author: auro005
"""

import numpy as np
from math import *
from numpy import *

def givens(a,b):
    if(b==0):
        c=1
        s=0
    else:
        if(abs(b)>abs(a)):
            r = a/b
            s = 1/(1+r**2)**0.5
            c = s*r
        else:
            r = b/a
            c = 1/(1+r**2)**0.5
            s = c*r
    return(c,s)

A = np.matrix([[4.0,7,2,4,7,3,6],[8,1,3,8,7,6,1],[8,5,2,5,7,1,3],[2,7,4,3,8,6,2],[7,8,7,6,8,8,2]])
####change the above line
m,n = A.shape

Q = np.identity(m)

R = A
#print(R)
#print(R[0:3])
for j in range(0,n,1):
    for i in range(m-1,j,-1):
        G = np.identity(m)
        
        c,s = givens(R[i-1,j],R[i,j])
        G[i-1:i+1,i-1:i+1] = [[c,-s],[s,c]]
        
        R = matmul(G.transpose(),R)
        Q = matmul(Q,G)

print(Q)
print(R)        
print(np.linalg.norm(np.identity(5)-(matmul(Q.transpose(),Q))))

print(np.linalg.norm(A-matmul(Q,R)))
