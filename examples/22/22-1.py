# File 22-1.py
# Example 22. Amino acid solution
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import numpy as np
from scipy.optimize import fsolve

# low pH ----------------------------> high pH
# +H3N-R-COOH <=> +H3N-R-COO- <=> H2N-R-COO-
# R1 <=> R2 <=> R3
def model(X):
    R1, R2, R3, H, OH = X
    Kw = 1e-14
    Ka1 = 10**-2.3
    Ka2 = 10**-9.8
    c = 0.1                        # alanine concentration, mol/L
    eq1 = R2*H/R1 - Ka1 
    eq2 = R3*H/R2 - Ka2
    eq3 = H*OH - Kw
    eq4 = H + R1 - R3 - OH
    eq5 = c - R1 - R2 - R3
    return [eq1, eq2, eq3, eq4, eq5]

R1, R2, R3, H, OH = fsolve(model, [1e-4, 1e-2, 1e-4, 1e-5, 1e-6])
pH = -np.log10(H)
print "Alanine 0.1 mol/L"
print "[cationic form]={:.3e} mol/L".format(R1) 
print "[zwitterion form]={:.3e} mol/L".format(R2) 
print "[anionic form]={:.3e} mol/L".format(R3) 
print "pH={:.2f}".format(pH)
