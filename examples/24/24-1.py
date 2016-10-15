# File 24-1.py
# Example 24. Mixture of a weak acid and a strong base
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import numpy as np
from scipy.optimize import fsolve

# initially:
# 0.1mol CH3COOH + 0.05mol KOH in 1L
# pH=?
def model(X):
    HA, A, K, H, OH = X
    Kw = 1e-14
    Ka = 10**-4.756                      # pKa = 4.756
    c1 = 0.1 # mol/L CH3COOH
    c2 = 0.05 # mol/L KOH

    eq1 = A*H - HA*Ka                    # dissociation constant in a product form
    eq2 = H*OH - Kw                      # water ionization product   
    eq3 = H + K - A - OH                 # charge balance
    eq4 = c1 - A - HA                    # the acid balance
    eq5 = K - c2                         # the potassium cation balance
    return [eq1, eq2, eq3, eq4, eq5]

HA, A, K, H, OH = fsolve(model, [1e-5, 1e-5, 0.05, 1e-5, 1e-5])
print HA, A, K, H, OH  # see if values (results) have chemical sense  
pH = -np.log10(H)
print "pH={:.2f}".format(pH)
