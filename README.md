# graphing-toolkit
This is a toolkit I'm working on under a professor at UMass Lowell as part of a scholarship. The purpose of this project is to create a toolkit specializing in solving differential equations. As of right now, the program is very basic and only graphs the contour plot of some function F(x,y).

May 20, 2019: 
A few changes were made to the code today which revamped how the function is plotted. This was done due to the old way having issues with negative numbers being inputted into the starting/ending values of x and y. One example of how this was done was switching from numpy.arrange to numpy.linspace for treating the ranges of x and y. As of right now, "dx" and "dy" are set in stone, but will later be changeable by user given the GUI.

![Demo of the Applicaton as of May 20, 2019](https://github.com/jbaig77/graphing-toolkit/blob/master/images/demo.png)
