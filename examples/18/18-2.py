# File 18-2.py
# Example 18. Effect of inert gases on the equilibrium composition
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

# one unknown one equation
# EB <=> S + H2
def model1(x):
    xe = x                 #equilibrium conversion
    Kp = 0.099 
    n0EB = 1
    n0H2O = 10             # steam (inert)
    P = 0.1                # MPa
    P0 = 0.1               # MPa

    # at equilibrium
    nEB = n0EB - xe 
    nS = xe
    nH2 = xe
    nTotal = nEB + nS + nH2 + n0H2O # = 11+xe
    
    yEB = nEB/nTotal
    yS = nS/nTotal
    yH2 = nH2/nTotal

    eq1 = (yS*yH2/yEB) * (P/P0) - Kp 
    return eq1

 
guess = 0.5
xe, = fsolve(model1, guess)
print "Model1 EB+steam 1:10 molar ratio"
print "Equilibrium conversion: {:.2f}".format(xe)
