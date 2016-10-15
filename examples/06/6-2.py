# File 6-2.py
# Example 6. Solving algebraic equation(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
import numpy as np

def equation(x):
    eq =  x**3 - 2*x**2 - 9*x + 10
    return eq

guess = 6
x1, = fsolve(equation, guess)
print "x1={}".format(x1)              # the solution no.1
guess = 0
x2, = fsolve(equation, guess)
print "x2={}".format(x2)              # the solution no.2
guess = -10
x3, = fsolve(equation, guess)
print "x3={}".format(x3)              # the solution no.3

