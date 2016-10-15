# File 20-2.py
# Example 20. Weak electrolyte equilibrium
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
from numpy import log10

# H2A <=> HA- + H+
# HA- <=> A2- + H+
def model(X, C_H2A):
    h, oh, h2a, ha, a = X
    c_h2a = C_H2A
    Kw = 1e-14
    # dissociation constants for itaconic acid
    Ka1 = 10**-3.85
    Ka2 = 10**-5.45

    eq1 = h*oh - Kw                    # water ionization constant 
    eq2 = h - oh - ha - 2*a            # the electroneutrality constraint
    eq3 = h*ha/h2a - Ka1               # dissociation process
    eq4 = h*a/ha - Ka2                 # dissociation process
    eq5 = c_h2a - h2a - ha - a         # the acid balance 
    return [eq1, eq2, eq3, eq4, eq5]

C_H2A = 0.1 # mol/L

# h, oh, h2a, ha, a
guess = [1e-2, 1e-5, 1e-2, 1e-5, 1e-5]          # experiment with realistic values
h, oh, h2a, ha, a = fsolve(model, guess, C_H2A) # check sense of the results (>0?) 
pH = -log10(h)

print "Equilibrium concentrations (cH2A=0.1mol/L):"
print "[H+]={:.2e} mol/L".format(h)
print "[OH-]={:.2e} mol/L".format(oh)
print "[H2A]={:.2e} mol/L".format(h2a)
print "[HA-]={:.2e} mol/L".format(ha)
print "[A2-]={:.2e} mol/L".format(a)
print "pH={:.2f}".format(pH)
