# File 20-1.py
# Example 20. Weak electrolyte equilibrium
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
from numpy import log10

def model(X, C_HA):
    h, oh, ch3cooh, ch3coo = X
    c_ch3cooh = C_HA
    Kw = 1e-14
    Ka = 1.8e-5

    eq1 = h*oh - Kw                    # water ionization constant 
    eq2 = h - oh - ch3coo              # the electroneutrality constraint
    eq3 = h*ch3coo/ch3cooh - Ka        # dissociation process
    eq4 = c_ch3cooh - ch3cooh - ch3coo # acetic acid balance 
    return [eq1, eq2, eq3, eq4]

C_HA = 0.5 # mol/L
# h, oh, ch3cooh, ch3coo
guess = [1e-2, 1e-5, 1e-2, 1e-2]       # experiment with different, but realistic values
h, oh, ch3cooh, ch3coo = fsolve(model, guess, C_HA)
pH = -log10(h)
print "Equilibrium concentrations (cCH3COOH=0.5mol/L):"
print "[H+]={:.2e} mol/L".format(h)
print "[OH-]={:.2e} mol/L".format(oh)
print "[CH3COOH]={:.2e} mol/L".format(ch3cooh)
print "[CH3COO-]={:.2e} mol/L".format(ch3coo)
print "pH={:.2f}".format(pH)
