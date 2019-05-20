import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import *

fields = 'xo', 'xf', 'yo', 'yf', 'Function'

def func(x,y,func):
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

   x = np.linspace(xo, xf, 50)
   y = np.linspace(yo, yf, 50)

   plt.figure()

   X,Y = np.meshgrid(x, y)
   Z = func(X, Y, f)

   plt.contourf(X,Y,Z,20,cmap='RdGy')
   plt.colorbar()
   plt.show()
