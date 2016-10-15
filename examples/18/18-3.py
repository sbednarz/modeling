# File 18-3.py
# Example 18. Effect of inert gases on the equilibrium composition
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt 
from scipy.optimize import fsolve
import numpy as np

# one unknown one equation
# EB <=> S + H2
def model1(x, steam):
    xe = x                 #equilibrium conversion
    Kp = 0.099 
    n0EB = 1
    n0H2O = steam          # steam (inert)
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


steam_amounts = np.linspace(0,50)
results = np.array([])             # to save calculated xe

for steam in steam_amounts: 
    guess = 0.5
    xe, = fsolve(model1, guess, steam)
    results = np.append( results, xe )

plt.plot(steam_amounts, results, 'gv')
plt.xlabel('steam:EB molar ratio')
plt.ylabel('EB equilibrium conversion')
plt.title('18-3.pdf')
plt.savefig('18-3.pdf')
plt.close()

