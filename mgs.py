# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 23:11:24 2021

@author: AUROBINDA
"""

import numpy as np
from math import *
from matplotlib.pylab import *
from numpy import *

A = np.matrix([[4.0,7,2,4,7,3,6],[8,1,3,8,7,6,1],[8,5,2,5,7,1,3],[2,7,4,3,8,6,2],[7,8,7,6,8,8,2]])

m,n = A.shape
q = np.matrix(A)
u_1 = A[:,0]
r = np.matrix([[0.0]*n]*n)
for k in range(0,n,1):
    r_k = (np.linalg.norm(q[:,k]))
    r[k,k] = r_k
    q[:,k] = q[:,k]/r_k
    for j in range(k+1,n,1):
        r[k,j] = (sum(matmul(q[:,k].transpose(),q[:,j])))
        q[:,j] = q[:,j]-r[k,j]*q[:,k]

print(np.linalg.norm(np.identity(7)-(matmul(q.transpose(),q))))

print(np.linalg.norm(A-matmul(q,r)))