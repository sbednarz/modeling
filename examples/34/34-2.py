# File 34-2.py
# Example 34. Kinetic model for oxidation process (2)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License 

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.integrate import odeint

# A + B -> C, k1
# B + C -> D, k2
# B - an oxidant, C - desired, D - undesired product

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


def run_simulation(b0):
    A0=1.0
    B0=b0
    C0=0
    D0=0
    ic = [A0, B0, C0, D0] # initial conditions
    t = np.linspace(0, t_max,N)
    results = odeint( model, ic, t)
    A = results[:,0]
    B = results[:,1]
    C = results[:,2]
    D = results[:,3]
    return D

N = 150
t_max = 5 #h
B0_min = 0
B0_max = 3

data = np.empty([0,N])
b0_range = np.linspace(B0_min, B0_max, N)
for b0 in b0_range:
    D = run_simulation(b0)
    data = np.insert(data, 0, D, axis=0) # insert rows in reversed order

fig, ax = plt.subplots()
#imgplot = ax.imshow(data, cmap=cm.viridis)
imgplot = ax.imshow(data, interpolation='none', cmap=cm.jet)
cbar = fig.colorbar(imgplot, ticks=[0,0.5, 0.9])
cbar.set_label('D, mol/L')
ax.set_xticks([0,N/2.0,N])
ax.set_xticklabels([0,t_max/2.0,t_max])
ax.set_xlabel('Reaction time, h')
ax.set_yticks([0, N/2.0, N])
ax.set_yticklabels([B0_max, (B0_max-B0_min)/2.0, B0_min])
ax.set_ylabel('B0, mol/L')
ax.set_title('Fig. 34-3.pdf')
plt.savefig('34-3.pdf')
plt.close()

