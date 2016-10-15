# File 19-1.py
# Example 19. Strong electrolyte equilibrium
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
from numpy import log10

def model(X, C_HCL):
    h, oh, cl = X
    c_hcl = C_HCL
    Kw = 1e-14
    
    eq1 = h*oh - Kw              # ion product of water 
    eq2 = h - cl - oh            # the electroneutrality constraint
    eq3 = c_hcl - cl             # chlorine balance
    return [eq1, eq2, eq3]

c_hcl = 1e-1 # mol/L
guess = [1e-5, 1e-5, 1e-5]       # h, oh, cl
h, oh, cl = fsolve(model, guess, c_hcl)
pH = -log10(h)

print "Equilibrium concentrations (cHCL=0.1mol/L):"
print "[H+]={:.2e} mol/L".format(h)
print "[Cl-]={:.2e} mol/L".format(cl)
print "[OH-]={:.2e} mol/L".format(oh)
print "pH={:.2f}".format(pH)


c_hcl = 1e-7 # mol/L (only theoretically possible)
guess = [1e-5, 1e-5, 1e-5]        # h, oh, cl
h, oh, cl = fsolve(model, guess, c_hcl)
pH = -log10(h)

print "Equilibrium concentrations (cHCL=1e-7mol/L):"
print "[H+]={:.2e} mol/L".format(h)
print "[Cl-]={:.2e} mol/L".format(cl)
print "[OH-]={:.2e} mol/L".format(oh)
print "pH={:.2f}".format(pH)

