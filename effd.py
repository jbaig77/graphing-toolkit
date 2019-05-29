'''
delta x = dx
starting x = xo
x at i = xi
y at i = yi
y at i+1 = yi2

Equation to Solve: 3(dy/dx) + 4y = 3x^2
@ x = 0, y = 10
x ranges from 0 to 10

general formula for yi2:
yi2 = dx*(xi**2) - ((4 * dx)/3)*yi + yi
'''

import numpy as np
from matplotlib import pyplot as plt
from array import *

global xo
global yo
global xf

def function(dx):
    n = int((xf-xo)/dx)+1

    x = np.linspace(0,10,n)
    y = np.zeros([n])

    y[0] = 10

    for i in range(0,n-1,1):
        a = 3
        b = 4
        f = 0
        y[i+1] = (f-b*y[i])*dx/3. + y[i]
        #y[i+1] = dx*(x[i]**2) - ((4 * dx)/3)*y[i] + y[i]
    return x, y

xo = 0
yo = 10
xf = 10

x1, y1 = function(1)
x2, y2 = function(0.5)
x3, y3 = function(0.25)
x4, y4 = function(0.1)
x5, y5 = function(0.01)
x6, y6 = function(0.001)

plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'g')
plt.plot(x3, y3, 'r')
plt.plot(x4, y4, 'c')
plt.plot(x5, y5, 'm')
plt.plot(x6, y6, 'y')

plt.show()
