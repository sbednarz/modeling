# File 49-3.py
# Example 49. Enzymatic reaction kinetics
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Simple enzymatic reaction 
# E + S <-> ES, k1, k2
# ES -> E + P, k3
def model(y, t):
    E = y[0]                   # unpack variables
    S = y[1]
    ES = y[2]
    P = y[3]
    dEdt = -k1*E*S + k2*ES + k3*ES
    dSdt = -k1*E*S + k2*ES
    dESdt = k1*E*S - k2*ES - k3*ES
    dPdt = k3*ES
    return [dEdt, dSdt, dESdt, dPdt]  # return derivatives  

k1 = 500
k2 = 6
k3 = 1.5


S0 = 0.0001           # experiment with different values
E0 = 0.00001

ic = [E0, S0, 0, 0]
t = np.linspace(0,6000)
results = odeint( model, ic, t)
E = results[:,0]
S = results[:,1]
ES = results[:,2]
P = results[:,3]

KM = (k2+k3)/k1
Vmax = k3*E0

# exact rate of substrate uptake 
rS = -k1*E*S + k2*ES
# M-M approximation (for steady state)
rMM = Vmax*S/(KM+S)

plt.subplots_adjust(hspace = 0.5, left=0.2, right=0.9)
ax1 = plt.subplot(211)
ax1.set_title('49-3.pdf')
ax1.plot(t, S, 'co-', label='S')
ax1.plot(t, P, 'go-', label='P')
ax1.legend()
ax1.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax1.set_ylabel('Conc., mol/L')
ax2 = plt.subplot(212)
ax2.plot(t, -rS, 'yo-', label='rS')
ax2.plot(t, rMM, 'r-', label='rMM')
ax2.legend()
ax2.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax2.set_xlabel('Reaction time, s')
ax2.set_ylabel('Rate, mol/Ls')
plt.savefig('49-3.pdf')
plt.close()

