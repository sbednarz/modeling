# File 21-1.py
# Example 21. Hydrolysis of a salt
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import numpy as np
from scipy.optimize import fsolve

# pH 0.5mol/L sodium acrylate
# NaA => Na+ + A-; A- <=> HA + OH-
def model(X):
    Na, A, HA, H, OH = X
    Kw = 1e-14
    Ka = 10**-4.25 
    c = 0.5

    eq1 = A*H/HA - Ka                 # dissociation constant 
    #eq1 = A*H - HA*K  <-- this form of Ka expression is recommended for more complex systems
    eq2 = H*OH - Kw                   # water ion product
    eq3 = c - A - HA                  # the acid balance 
    eq4 = Na + H - A - OH             # charge balance
    eq5 = Na - c                      # it is obvious
    return [eq1, eq2, eq3, eq4, eq5]

Na, A, HA, H, OH = fsolve(model, [0.5, 1e-4, 1e-4, 1e-4, 1e-4])
pH = -np.log10(H)
print '0.5 mo/L sodium acrylate'
print '[Na+]={:.4e} mol/L'.format(Na)
print '[A-]={:.4e} mol/L'.format(A)
print '[HA]={:.4e} mol/L'.format(HA)
print '[OH-]={:.4e} mol/L'.format(OH)
print '[H+]={:.4e} mol/L'.format(H)
print 'pH={:.2f}'.format(pH)
