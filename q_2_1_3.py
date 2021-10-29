# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:20:29 2021

@author: AUROBINDA
"""

import numpy as np
from math import *
from matplotlib.pylab import *

alpha = 0.001
m = 5
rat = alpha/m
table_8_2 = np.array([[-1, 2, 51.5073, 0.1290, 36, 89.563],
[-1, 3, 51.5074, 0.1275, 47, 123.543],
[+1, 1, 51.5071, 0.1278, 26, 23.989],
[-1, 1, 51.5075, 0.1281, 68, 138.769],
[+1, 2, 51.5074, 0.1278, 33, 113.888]])

p = np.concatenate(((np.ones(5)), table_8_2[:,0], table_8_2[:,1], table_8_2[:,4]))
x = p.reshape(4,5)
y = x.transpose()

print(y)
a = y[:,0] + y[:,1] + y[:,2] + y[:,3] - table_8_2[:,-1]

print(sum(a*x[0,:]))
theta_0 = -1.0
theta_1=-1.0
theta_2 = -1.0
theta_3=-1.0

for i in range(0,100000,1):
    a = theta_0*y[:,0] + theta_1*y[:,1] + theta_2*y[:,2] + theta_3*y[:,3] - table_8_2[:,-1]
    theta_0 = theta_0 - rat*(sum(a*x[0,:]))
    theta_1=theta_1 - rat*(sum(a*x[1,:]))
    theta_2 = theta_2 - rat*(sum(a*x[2,:]))
    theta_3=theta_3 - rat*(sum(a*x[3,:]))

print(theta_0,theta_1,theta_2,theta_3)

print(theta_0+theta_1+(2.0*theta_2)+(60*theta_3))
print(theta_0-theta_1+(2.0*theta_2)+(60*theta_3))

print(theta_0+theta_1+(3.0*theta_2)+(60*theta_3))
print(theta_0-theta_1+(3.0*theta_2)+(60*theta_3))

print(theta_0+theta_1+(1.0*theta_2)+(60*theta_3))
print(theta_0-theta_1+(1.0*theta_2)+(60*theta_3))
