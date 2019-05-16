import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import time

def function(x,y):
    return x**2 + y**2
'''
def length(a):
    return len(a)

def getZ(x,y):
    Z = [[0 for c in range(length(x))] for d in range(length(y))]
    for i in range(0,99):
        for j in range(0,99):
            Z[i][j] = functions(x[j] + j, y[i] + i)
    return Z
'''
def plot(x,y):
    x = np.arange(0,1,0.01)
    y = np.arange(0,1,0.01)
    plt.figure()
    lx = len(x)
    ly = len(y)
    X,Y = np.meshgrid(x,y)
    Z = [[0 for c in range(lx)] for d in range(ly)]
    for i in range(0,99):
        for j in range(0,99):
            Z[i][j] = function(x[j]+j, y[i]+i)
    plt.contour(X,Y,Z,100)
    plt.grid(True)
    plt.show()

start = time.time()

def multiP():
    p = mp.Process(target=plot, args = (1,1))
    p.start()

if __name__ == "__main__":
    multiP()

end = time.time()

print(end-start)
