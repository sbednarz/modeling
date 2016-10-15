# File 13-2.py
# Example 13. Differential mass balance
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# model = mass balance = ODE (or ODEs)
def model(y, t):
    h = y[0]
    dhdt = Fin/A - Fout/A
    return [dhdt]

Fin = 1 #m3/min
Fout = 0.8 #m3/min
A = 5.0 # m3
t = np.linspace(0,60) # 0 - 60 min

ic = [0] # initial conditions: h at t=0 -> h0=0 

results = odeint(model, ic, t)
h = results[:,0]
print "Time, min"
print t
print "h(t), m"
print h # h(t)

plt.plot(t,h, 'b.')
plt.xlabel('Time, min')
plt.ylabel('Liquid level (h), m')
plt.savefig('13-2.pdf')
plt.close()
