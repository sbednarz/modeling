# File 34-a.py
# Example 34. Kinetic model for oxidation process (2)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License 

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# A + B -> C, k1
# B + C -> D, k2
# A - a substrate, B - an oxidant, C - desired, D - undesired product

def model(y, t):
    A = y[0]
    B = y[1]
    C = y[2]
    D = y[3]
    #rate constants
    k1 = 1e-3*3600
    k2 = 1e-4*3600
    # ODEs
    dAdt = -k1*A*B
    dBdt = -k1*A*B
    dCdt = k1*A*B - k2*B*C
    dDdt = k2*B*C
    return [dAdt, dBdt, dCdt, dDdt]

A0=1.0
B0=3.0
C0=0
D0=0
ic = [A0, B0, C0, D0] # initial conditions
t = np.linspace(0,5)
results = odeint( model, ic, t)
A = results[:,0]
B = results[:,1]
C = results[:,2]
D = results[:,3]

alpha = 100*A/A0
Y = 100*C/A0
S = 100*C/(C+D)

fig,ax = plt.subplots()
ax.set_title('Fig. 34-2.pdf')
ax.plot(t ,A, label='A')
ax.plot(t ,B, label='B')
ax.plot(t ,C, label='C')
ax.plot(t ,D, label='D')
ax.legend(loc='upper right', ncol=4)
ax.set_ylim([0,3.0])
ax.set_yticks([0,1.5,3.0])
ax.set_ylabel('Conc., mol/L')
ax.set_xlabel('Reaction time, h')

ax.annotate('deep red', xy=(0.3, 0.8), xytext=(0.4, 1),
        arrowprops=dict(arrowstyle='->'))

ax.annotate('yellow', xy=(1, 0.5), xytext=(1.1, 0.7),
        arrowprops=dict(arrowstyle='->'))

ax.annotate('blue', xy=(2, 0.3), xytext=(2.1, 0.5),
        arrowprops=dict(arrowstyle='->'))

ax.annotate('deep blue', xy=(4.7, 0.1), xytext=(4.0, 0.3),
        arrowprops=dict(arrowstyle='->'))

ax.annotate('B0', xy=(0, 2.9), xytext=(-0.8,2.6), 
        arrowprops=dict(arrowstyle='->'))



plt.savefig('34-2.pdf')
plt.close()
