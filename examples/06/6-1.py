# File 6-1.py
# Example 6. Solving algebraic equation(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
import numpy as np

def equation(x):
    eq = np.sqrt(x) - 2.5
    return eq

guess = 1
x0, = fsolve(equation, guess)
print x0              # the solution
print equation(x0)    # the result checking, 0?
