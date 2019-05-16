import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import time


def function(x,y):
    return x**2 + y**2

start = time.time()

plt.figure()

#pool = mp.Pool(mp.cpu_count())

x = np.arange(0, 1, 0.01)
y = np.arange(0, 1, 0.01)

a = len(x)
b = len(y)

X,Y = np.meshgrid(x, y)

Zmatrix = [[0 for c in range(a)] for d in range(b)]

for i in range(0,99):
    for j in range(0, 99):
        #Zmatrix[i][j] = (x[j] + j)**2 + (y[i]+i)**2
        Zmatrix[i][j] = function(x[j] + j, y[i] + i)

plt.contour(X, Y, Zmatrix, 100)
plt.grid(True)
#plt.show()

end = time.time()

print(end-start)

plt.show()
