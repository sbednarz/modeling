# File 8-1.py
# Example 8. Mass balance (1)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

F1 = 1234 #kg/h
x1MeOH = 0.2
x2MeOH = 0
x2H2O = 1
x3MeOH = 0.05

def model(X):
    x1H2O, F2, F3, x3H2O = X
    eq1 = F1 + F2 - F3                             # material balance of the system
    eq2 = x1MeOH * F1 + x2MeOH * F2 - x3MeOH * F3  # MeOH balance
    eq3 = x1MeOH + x1H2O -1                        # mass fraction constraint
    eq4 = x3MeOH + x3H2O -1                        # mass fraction constraint
    return [eq1, eq2, eq3, eq4]

guess = [0.1, 100, 100, 0.1]
x1H2O, F2, F3, x3H2O = fsolve(model, guess)
print "x1H2O = {:.2f}".format(x1H2O)
print "F2 = {:.2f} kg/h".format(F2) 
print "F3 = {:.2f} kg/h, x3H2O = {:.2f}".format(F3, x3H2O)
