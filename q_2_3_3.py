# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:54:49 2021

@author: AUROBINDA
"""
#MAP Method age + gender + degree vs salary

import numpy as np
from math import *
from matplotlib.pylab import *

table_8_2 = np.array([[-1, 2, 51.5073, 0.1290, 36, 89.563],
[-1, 3, 51.5074, 0.1275, 47, 123.543],
[+1, 1, 51.5071, 0.1278, 26, 23.989],
[-1, 1, 51.5075, 0.1281, 68, 138.769],
[+1, 2, 51.5074, 0.1278, 33, 113.888]])
p = np.concatenate(((np.ones(5)), table_8_2[:,0], table_8_2[:,1], table_8_2[:,4]))
x = p.reshape(4,5)
y = x.transpose()
i=0.1
while(i<10):
    mat_mul = inv(np.matmul(y.transpose(),y) + (i)*np.identity(4))
    mat_mul_1 = np.matmul(mat_mul,y.transpose())
    mat_mul_final = np.matmul(mat_mul_1,table_8_2[:,-1])
    i = i+0.01
    theta_0 = mat_mul_final[0]
    theta_1 = mat_mul_final[1]
    theta_2 = mat_mul_final[2]
    theta_3 = mat_mul_final[3]
    f = open("gender and age and degree vs salary.txt","a")
    
    #print(matrix(table_8_2[:,4]).transpose())
    f.write(str(mat_mul_final[0]))
    f.write("\t")
    f.write(str(mat_mul_final[1]))
    f.write("\t")
    f.write(str(mat_mul_final[2]))
    f.write("\t")
    f.write(str(mat_mul_final[3]))
    f.write("\t")
    f.write(str(theta_0+theta_1+(2.0*theta_2)+(60*theta_3)))
    f.write("\t")
    f.write(str(theta_0+theta_1+(3.0*theta_2)+(60*theta_3)))
    f.write("\t")
    f.write(str(theta_0+theta_1+(1.0*theta_2)+(60*theta_3)))
    f.write("\t")
    f.write(str(theta_0-theta_1+(2.0*theta_2)+(60*theta_3)))
    f.write("\t")
    f.write(str(theta_0-theta_1+(3.0*theta_2)+(60*theta_3)))
    f.write("\t")
    f.write(str(theta_0-theta_1+(1.0*theta_2)+(60*theta_3)))
    f.write("\n")