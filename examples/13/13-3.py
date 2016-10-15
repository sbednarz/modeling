# File 13-3.py
# Example 13. Differential mass balance
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# model = mass balance = ODE
def model(y, t):
    V = y[0]
    dVdt = Fin
    return [dVdt]

m = 5.0                 # kg
M = 150.0               # kg/kmol
n = m/M                 # kmol
Fin = 0.5               # m3/h
t = np.linspace(0, 12)  # 0 - 12h

ic = [0]                # initial conditions: V at t=0 -> V0=0 
results = odeint(model, ic, t)
V = results[:,0]        # instant V
C = n/V                 # instant C
print "Time, h"
print t
print "V(t), m3"
print V
print "C(t), kmol/m3"
print C

plt.subplot(211)
plt.plot(t,V, 'bo-')
plt.xlabel('Time, h')
plt.ylabel('V, m$^3$')
plt.subplot(212)
plt.plot(t,C, 'mo-')
plt.xlabel('Time, h')
plt.ylabel('C, kmole/m$^3$')
plt.savefig('13-3.pdf')
plt.close()
