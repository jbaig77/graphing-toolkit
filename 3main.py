import numpy as np
import matplotlib.pyplot as plt
import math
import tkinter

class ButtonEntry():
    def __init__(self, root, xx):
        self_entry_var = ""

        startLabel = tkinter.Label(root, text = xx)
        self.startEntry = tkinter.Entry(root)

        startLabel.pack()
        self.startEntry.pack()
        self.startEntry.focus_set()

        self.writing()
        plotButton = tkinter.Button(root, text = "Write",command = self.writing).pack()

    def writing(self):
        self.entry_var = self.startEntry.get()
        print("inside class", self.entry_var)


def function(x,y,func):
    return eval(func)

def close_window():
    window.destroy()

root = tkinter.Tk()
root.title("Equation Grapher")

b1 = ButtonEntry(root, "Enter xo: ")
b2 = ButtonEntry(root, "Enter xf: ")
b3 = ButtonEntry(root, "Enter yo: ")
b4 = ButtonEntry(root, "Enter yf: ")
b5 = ButtonEntry(root, "Enter the function: ")

closing_button = tkinter.Button(root, text="Graph the function", command=root.destroy)
closing_button.pack()

root.mainloop()

xo = float(b1.entry_var)
xf = float(b2.entry_var)

yo = float(b3.entry_var)
yf = float(b4.entry_var)

Z = str(b5.entry_var)


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
        Zmatrix[i][j] = function(x[j] + j, y[i] + i, Z)

plt.contour(X, Y, Zmatrix, 100)
plt.show()
