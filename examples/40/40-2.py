# File 40-2.py
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

def model(y, t):                          # mole balance of A for an unsteady-state
    A = y[0]
    dAdt = - rA(A)
    return [dAdt]

#
A = np.linspace(0.1,200,200)
plt.plot(A, rA(A), 'm-', label='$r_{A}=f(A)$')
plt.xlabel('$[A]_0$, mol/m^3')
plt.ylabel('Rate, mol/(m^3 min)')

plt.axes([0.4, 0.46, 0.4, 0.3], axisbg='w')
A = np.linspace(0.1,20,100)
plt.plot(A, rA(A), 'm-')
plt.xlim(0, 20)
plt.xticks([0,5,10,15,20])
plt.yticks([0.0, 0.08, 0.16])
plt.xlabel('$[A]_0$')

plt.savefig('2.pdf')
plt.close()

t = np.linspace(0,18,100)
A0 = 1
results = odeint(model, [A0], t)
A = results[:,0]
plt.plot(t, A, label='[A]0 = 1 mol/m$^3$')
plt.xlabel('Time, s')
plt.ylabel('[A], mol/m^3')
plt.legend()
plt.savefig('2a.pdf')
plt.close()

t = np.linspace(0,2000,100)
A0 = 60
results = odeint(model, [A0], t)
A = results[:,0]
plt.plot(t, A, label='[A]0 = 60 mol/m$^3$')
plt.xlabel('Time, s')
plt.ylabel('[A], mol/m^3')
plt.legend()
plt.savefig('2b.pdf')
plt.close()

t = np.linspace(0,200000,100)
A0 = 600
results = odeint(model, [A0], t)
A = results[:,0]
plt.plot(t, A, label='[A]0 = 600 mol/m$^3$')
plt.xlabel('Time, s')
plt.ylabel('[A], mol/m^3')
plt.legend()
plt.savefig('2c.pdf')
plt.close()




