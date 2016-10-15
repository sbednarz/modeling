# File 36-1.py
# Example 36. Batch polymerization
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Stoichiometry:
# M -> P, k
# Empirical rate expresssion:
# -dM/dt = k*M**1.3
# rho = f (alpha): ro = 0.9 + alpha*0.1

# calculate conversion of the monomer (M)
def calcAlpha(nM):
    return (nM0-nM)/nM0

# calculate total volume of reaction mixture,
# based on initial mass and conversion of the monomer (M)
# and 'empirical' dependence of solution density 
# as a function of the solution composition rho=f(alpha)
def calcV(nM):
    alpha = calcAlpha(nM)
    ro = roM + (roP-roM)*alpha
    V = m0 / ro
    return V/1000.0             # to have volume in L

def model(y,t):                 # kinetic model
    nM = y[0]
                                # calculate instant values
    V = calcV(nM)               # volume of the mixture
    M = nM/V                    # molar concentration of M (substrate)
    
    dnMdt = -k*M**1.3*V         # calculate & return derivatives
    return [dnMdt]

# The model parameters
k = 4e-4*3600                   # polymerization rate coefficient
roM = 0.9                       # density of pure M 
roP = 1.0                       # density of pure P
nM0 = 8                         # initial amount of M (mole)
nP0 = 0                         # initial amount of P (mole)
MM = 104                        # molecular weight of M g/mol
m0 = nM0 * MM                   # initial mass of the monomer (g)

ic = [nM0]                      # initial conditions
t = np.linspace(0,3)
results = odeint(model, ic, t)

# post-processing of results
nM = results[:,0]               # nM(t)
V = calcV(nM)                   # V(t)
M = nM/V                        # calculate molar concentrations of M
alpha = calcAlpha(nM)
Vlim100 = calcV(0)              # V at 100% conversion, just to plot on graph
Vlim0 = calcV(8)                # V at 0% conversion, just to plot on graph

ax1 = plt.subplot(211)
ax1.set_xlim(0,3)
ax1.set_ylim(0,9)
ax1.set_xticks([])
ax1.set_yticks([0.0,3.0,6.0,9.0])
ax1.set_ylabel('[M], mol/L')
ax1.plot(t,M,'m-')
# plot V(t)
ax2 = plt.subplot(212)
ax2.set_xlim(0,3)
ax2.set_ylim(0.8,1)
ax2.set_xticks([0,1,2,3])
ax2.set_xlabel('Reaction time, h')
ax2.set_yticks([0.8, 0.9 , 1.0])
ax2.set_ylabel('V of mixture, L')
ax2.plot(t,V,'b-')
ax2.plot((0,3),(Vlim100, Vlim100),'b--') # just to make the graph nicer
ax2.plot((0,3),(Vlim0, Vlim0),'c--')     #
ax2.annotate("", xy=(0.7,0.835), xytext=(0.7,0.92), arrowprops=dict(arrowstyle='<->'))
ax2.text(0.8, 0.87, 'Volume\ncontraction')
plt.savefig('36-1.pdf')
plt.close()
