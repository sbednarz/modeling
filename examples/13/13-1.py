# File 13-1.py
# Example 13. Differential mass balance
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# model = mass balance = ODE (or ODEs)
def model(y, t):
    V = y[0]
    dVdt = Fin - Fout
    return [dVdt]

Fin = 10 #L/min
Fout = 1 #L/min
t = np.linspace(0,60) # 0 - 60 min

ic = [0] # initial conditions: V at t=0 -> V0=0 

results = odeint(model, ic, t)
V = results[:,0]
print "Time, min"
print t
print "V(t), L"
print V # V(t)

plt.plot(t,V, 'b.')
plt.xlabel('Time, min')
plt.ylabel('V, L')
plt.savefig('13-1.pdf')
plt.close()
