# File 18-1.py
# Example 18. Effect of inert gases on the equilibrium composition
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

# one unknown one equation
# EB <=> S + H2
def model1(x):
    xe = x             # equilibrium conversion
    Kp = 0.099 
    n0EB = 1
    P = 0.1            # MPa
    P0 = 0.1           # MPa

    # at equilibrium
    nEB = n0EB - xe 
    nS = xe
    nH2 = xe
    nTotal = nEB + nS + nH2 # = 1+xe
    
    yEB = nEB/nTotal
    yS = nS/nTotal
    yH2 = nH2/nTotal

    eq1 = (yS*yH2/yEB) * (P/P0) - Kp 
    return eq1

guess = 0.5
print "Model1 100%EB"
xe, = fsolve(model1, guess)
print "Equilibrium conversion: {:.2f}".format(xe)

# three unknowns three equations
# EB <=> S + H2
def model2(X):
    nEB, nS, nH2 = X # number of moles
    Kp = 0.099 
    n0EB = 1
    P = 0.1 # MPa
    P0 = 0.1 # MPa

    # at equilibrium
    nTotal = nEB + nS + nH2
    yEB = nEB/nTotal
    yS = nS/nTotal
    yH2 = nH2/nTotal
    eq1 = (yS*yH2/yEB) * (P/P0) - Kp 
    eq2 = n0EB - nEB - nS
    eq3 = nS - nH2
    return [eq1, eq2, eq3]

guess = [0.5,0.5,0.5]
print "Model2 100%EB"
yEB, yS, yH2 = fsolve(model2, guess)
print "Equilibrium mole fractions:"
print "yEB={:.2f}".format(yEB)
print "yS={:.2f}".format(yS)
print "yH2={:.2f}".format(yH2)
