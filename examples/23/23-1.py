# File 23-1.py
# Example 23. Hydrolysis of triprotic acid salt
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import numpy as np
from scipy.optimize import fsolve

# pH Na2HPO4 0.01mol/L
# HPO4 <=> PO4
# H2PO4 <=> HPO4
# H3PO4 <=> H2PO4
def model(X):
    H3A, H2A, HA, A, Na, H, OH = X
    Kw = 1e-14
    Ka1 = 10**-2.15
    Ka2 = 10**-7.12
    Ka3 = 10**-12.35
    c = 0.01 # mol/L

    eq1 = H2A*H - H3A*Ka1                        # dissociation constant in a product form
    eq2 = HA*H - H2A*Ka2                         # it makes numeric calculations more easily
    eq3 = A*H - HA*Ka3                           # 
    eq4 = H*OH - Kw
    eq5 = H + Na - 3*A - 2*HA - H2A - OH
    eq6 = c - A - HA - H2A - H3A
    eq7 = Na - 2*c                                # <---
    return [eq1, eq2, eq3, eq4, eq5, eq6, eq7]

H3PO4, H2PO4, HPO4, PO4, Na, H, OH = fsolve(model, [1e-6, 1e-6, 1e-6, 1e-6, 0.01, 1e-6, 1e-6])
print H3PO4              #
print H2PO4              #
print HPO4               #
print PO4                #
print Na                 #
print H                  #
print OH                 # see if values (results) have chemical sense  

pH = -np.log10(H)
print "pH={:.2f}".format(pH)
