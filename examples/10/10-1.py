# File 10-1.py
# Example 10. Mass balance with recycle (1)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

FM = 100 #kg/h
alfa = 0.3

def model(X):
    FP, FR = X                     # equivalent syntax: FP=X[0] FR=X[1] 
    eq1 = FM - FP                  # total mass balance
    eq2 = alfa*(1*FM + 1*FR) - FP  # monomer balance
    return [eq1, eq2]

guess = [100, 100] # FP FR
FP, FR = fsolve(model, guess)
print 'FP={:.2f} kg/h'.format(FP)
print 'FR={:.2f} kg/h'.format(FR)
