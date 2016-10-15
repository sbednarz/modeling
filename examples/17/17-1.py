# File 17-1.py
# Example 17. Esterification (3)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np

# a - alcohol, e - ester, w - water
def model(X, C_ACID):               # <--- note model has 2 arguments
    a, acid, e, w = X
    K = 4.9
    c_a = 16.0
    c_acid = C_ACID                 # Python is case-sensitive

    eq1 = (e*w)/(a*acid)-K          # equilibrium constant
    eq2 = a + e - c_a               # the alcohol balance
    eq3 = acid + e - c_acid         # the acid balance

    eq4 = e - w                     # number of ester bonds 
                                    # is equivalent to 
                                    # amount of water produced
    return [eq1, eq2, eq3, eq4]

# warming-up example
# alcohol, acid, ester, water
guess = [1, 1, 2, 2]                # try different guess values
a, acid, e, w = fsolve(model, guess, 3) # we pass to fsolve additional parameter
print a, acid, e, w
# end of warming-up example

print "Report, concentrations in mol/L"
print "ch3cooh_0\tetoh\t\tch3cooh\t\tch3cooet\twater"
# initial acid concentration = 1-3 mol/L
concentrations = np.linspace(1,3,10)
# array prepared to save the results
ester_concentrations = np.array([])  

# calculations loop
for C_ACID in concentrations:
    # alcohol, acid, ester, water
    guess = [10, 0.1, 2, 2]       # put here most realistic guess values
    a, acid, e, w = fsolve(model, guess, C_ACID)
    print "{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}".format(C_ACID, a, acid, e, w)
    ester_concentrations = np.append(ester_concentrations, e)

# and graphical report
plt.plot(concentrations, ester_concentrations, 'bo') # excess of EtOH => linear dependence
plt.xlabel('c0 ch3cooh, mol/L')
plt.ylabel('ch3cooet at equlibrium, mol/L')
plt.savefig('17-1.pdf')
plt.close()
