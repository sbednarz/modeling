# File 11-1.py
# Example 11. Mass balance with recycle (2)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

from scipy.optimize import fsolve

FM = 100 #kg/h
alpha = 0.6

def model(X):
    FP, FR = X
    eq1 = (1-alpha)*(FM + FR) - FR - 0.05*FP # monomer balance 
    eq2 = alpha*(FM + FR) - 0.95*FP          # polymer balance
    return [eq1, eq2]

guess = [100,100] # FP, FR
FP, FR = fsolve(model, guess)
print 'FP={:.2f} kg/h'.format(FP)
print 'FR={:.2f} kg/h'.format(FR)
