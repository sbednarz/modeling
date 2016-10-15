# File 40-1.py
# Example 40. Multiple steady states
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint 
from scipy.optimize import fsolve

# rate of substrate A consumption
def rA(A):
    k1 = 0.25 # 1/min
    k2 = 0.43 # m^3/mol
    return k1*A/(1 + k2*A)**2 

# mass balance: in - out 
def net(A):
    return F*(Af - A)

def steadystate(y):                       # mole balance for a steady-state
    A = y[0]
    eq1 = net(A) - rA(A)*V                # mole balance of A
    return [eq1]

def model(y, t):                          # mole balance of A for an unsteady-state
    A = y[0]
    dAdt = net(A) - rA(A)*V
    return [dAdt]

V = 60 # m^3
F = 70e-3 # m^3/min
# [A] in the feed
Af = 69 # mol/m^3


x1, = fsolve(steadystate,[1])            #guess values: 1, 20, 50
x2, = fsolve(steadystate,[20])
x3, = fsolve(steadystate,[50])
print x1, x2, x3

t = np.linspace(0,250,100)

# [A] in the reactor at t=0
A0 = 15 # mol/m^3
results = odeint(model, [A0], t)
plt.plot(t, results[:,0], label='[A]0 = 15 mol/m$^3$')
plt.xlabel('Time, s')
plt.ylabel('[A], mol/m^3')
plt.legend()
plt.savefig('40-1a.pdf')
plt.close()

# [A] in the reactor at t=0
A0 = 60 # mol/m^3
results = odeint(model, [A0], t)
plt.plot(t, results[:,0], label='[A]0 = 60 mol/m$^3$')
plt.xlabel('Time, s')
plt.ylabel('[A], mol/m^3')
plt.legend()
plt.savefig('40-1b.pdf')
plt.close()

A = np.linspace(0,70,200)
plt.plot(A, net(A), 'g-', label='net flow rate A')
plt.plot(A, rA(A)*V, 'y-', label='A reacted')
plt.xlabel('[A], mol/m^3')
plt.ylabel('Rate, mol/(min m^3)')
plt.ylim(0,10)
plt.plot(x1,0,'rD')
plt.plot(x2,0,'rD')
plt.plot(x3,0,'rD')
plt.legend()
plt.savefig('40-1c.pdf')
plt.close()

