# File 14-1.py
# Example 14. Esterification (1)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
# a - alcohol, e - ester, w - water
def model(X):
    a, acid, e, w = X
    K = 4.9                         # equilibrium constant
    c_a = 16.0                      # mol/L EtOH
    c_acid = 3.0                    # mol/L, CH3COOH
    eq1 = (e*w)/(a*acid)-K          # equilibrium constant
    eq2 = a + e - c_a               # the alcohol balance
    eq3 = acid + e - c_acid         # the acid balance
    eq4 = e - w                     # number of ester bonds is equivalent to 
                                    # amount of water produced
    return [eq1, eq2, eq3, eq4]

a = 1.0
acid = 1.0
e = 2.0
w = 2.0
guess = [a, acid, e, w]
a, acid, e, w = fsolve(model, guess)
print "Equilibrium concentrations:"
print "[EtOH]={:.2f} mol/L".format(a)
print "[CH3COOH]={:.2f} mol/L".format(acid)
print "[CH3COOEt]={:.2f} mol/L".format(e)
print "[H2O]={:.2f} mol/L".format(w)
