# File 6-4.py
# Example 6. Solving algebraic equation(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
import numpy as np

def system( unknowns ):
    x = unknowns[0]       # unpack x
    y = unknowns[1]       # unpack y
    eq1 = y - x**2 - 2*x  # calculate eq1 for given x,y
    eq2 = y - 12 + x**2   # calculate eq2 for given x,y
    return [eq1, eq2]     # return the results (0?)

guess = [1, 1]                            # two unknowns = two guess; in order: x, y 
x0, y0 = fsolve(system, guess)
print "x0, y0 = {} {}".format(x0, y0)
guess = [-10, -10]                        # different pair of guess values
x1, y1 = fsolve(system, guess)
print "x1, y1 = {} {}".format(x1, y1)
