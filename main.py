import numpy as np
import matplotlib.pyplot as plt
import math
import tkinter

from tkinter import *
fields = 'xo', 'xf', 'yo', 'yf', 'Function'

def function(x,y,func):
    return eval(func)

def getVal(entries, text):
    a = float(entries[text].get())
    return a

def getFunc(entries):
    f = str(entries['Function'].get())
    return f

def hur(entries):
    global xo
    global xf
    global yo
    global yf
    global f
    xo = getVal(entries, 'xo') 
    xf = getVal(entries, 'xf') 
    yo = getVal(entries, 'yo') 
    yf = getVal(entries, 'yf') 
    f = getFunc(entries)
    root.quit()

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   root.title("Equation Grapher")
   ents = makeform(root, fields)
   b1 = Button(root, text='Calculate',
          command=(lambda e=ents: hur(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

   print (xo)
   print (xf)
   print (yo)
   print (yf)
   print (f)


#getting "dx" and "dy"
dx = float(xf - xo) / 100
dy = float(yf - yo) / 100

x = np.arange(xo, xf, dx)
y = np.arange(yo, yf, dy)

plt.figure()
a = len(x)
b = len(y)

X,Y = np.meshgrid(x, y)

Zmatrix = [[0 for c in range(a)] for d in range(b)]

for i in range(0, int(math.floor(xf/dx) - 1)):
    for j in range(0, int(math.floor(yf/dy) - 1)):
        Zmatrix[i][j] = function(x[j] + j, y[i] + i, f)

plt.contour(X, Y, Zmatrix, 100)
plt.show()
