# File 9-1.py
# Example 9. Mass balance (2)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

F1 = 20 #kmol/h

# acetone mass fractions
x1a = 2.0/100
x2a = 80.0/100
x3a = 0.08/100

def model(X):
    F2, F3 = X
    eq1 = F1 - F2 - F3
    eq2 = x1a * F1 - x2a * F2 - x3a * F3
    return [eq1, eq2]

guess = [1, 1] # F2, F3
F2, F3 = fsolve(model, guess)
print "Distilate F2 = {:.2f} kmol/h".format(F2)
print "Bottom fraction F3 = {:.2f} kmol/h.".format(F3)
