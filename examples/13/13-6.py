# File 13-6.py
# Example 13. Differential mass balance
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def model(y,t):
	V = y[0]
	dVdt = - r_evap
	return [dVdt]

# Model parameters
r_evap = 50              # Evaporation rate 50 L/h
V0=100                   # 100L at t=0
n0A=100                  # 100 mol A, 100mol/100L = 1mol/L

initial = [V0]
t = np.linspace(0,1)
results = odeint(model, initial, t)

V = results[:,0]         # V(t)
A = n0A/V                # A(t) mol/L

plt.figure()

# plot V=f(t)
plt.subplot(211)
plt.title('Fig. 13-1.pdf')
plt.ylim(0,140)
plt.plot(t,V,'m-', label='V')
plt.ylabel('Volume, L')
plt.legend()

# plot A=f(t)
plt.subplot(212)
plt.plot(t,A,'b-',label='[A] mol/L')
plt.ylabel('[A], mol/L')
plt.xlabel('Time, hour')
plt.legend(loc='upper left')
plt.savefig('13-6.pdf')
plt.close()
