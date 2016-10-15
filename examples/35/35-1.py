# File 35-1.py
# Example 35. Filling a batch reactor
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def model1(y,t):
	A = y[0]
	dAdt = (0.12-(0.56 + 0.015*t)*A)/(2+0.06*t)
	return [dAdt]

A0 = 0
t = np.linspace(0,30)
results = odeint(model1, [A0], t)
A = results[:,0]
plt.plot(t,A,'go-')
plt.title('35-1a.pdf')
plt.xlabel('Time, min')
plt.ylabel('[A], kmol/m3')
plt.text(10, 0.07, 'Model 1')
plt.savefig('35-1a.pdf')
plt.close()


def model2(y,t):
    V = y[0]                              # instant total volume
    nA = y[1]                             # instant mole numbers
    cA = nA/V                             # instant concentration, kmol/m3
    dVdt = 0.06                           # rate of change of the volume
    dnAdt = 0.06*2 - k*cA*V               # mole balance: flow_in - consumed_in_rxn
    return [dVdt, dnAdt]                  # note the rate definition: V dN/dt = r 

Fin = 0.06                                # m3/min
k = 0.25                                  # 1/min
nA0 = 0                                   # 
V0 = 2                                    # m3
t = np.linspace(0,30) #
results = odeint(model2, [V0, nA0], t)
V = results[:,0]                          # V(t)
nA = results[:,1]                         # nA(t)
cA = nA/V                                 # calculation of the concentration (!)
plt.plot(t,cA,'bo-')
plt.title('35-1b.pdf')
plt.xlabel('Time, min')
plt.ylabel('[A], kmol/m3')
plt.text(10, 0.07, 'Model 2')
plt.savefig('35-1b.pdf')
plt.close()
