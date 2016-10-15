# File 34-1.py
# Example 34. Kinetic model for oxidation process (2)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
from matplotlib import cm
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
    k1 = 3.60
    k2 = 0.36
    # ODEs
    dAdt = -k1*A*B
    dBdt = -k1*A*B
    dCdt = k1*A*B - k2*B*C
    dDdt = k2*B*C
    return [dAdt, dBdt, dCdt, dDdt]

def run_simulation(b0):                    # simulate the reaction
    A0=1.0                                 # for given B0
    B0=b0
    C0=0
    D0=0
    ic = [A0, B0, C0, D0]                  # initial conditions
    t = np.linspace(0, t_max,N)            # time span
    results = odeint( model, ic, t)        # results - concentrations(t)
    C = results[:,2]
    D = results[:,3]
    return C

N = 150                                    # number of steps
t_max = 5                                  # reaction time in hour
B0_min = 0                                 # B0 start
B0_max = 3                                 # B0 end

data = np.empty([0,N])                     # prepare matrix for results: D(B0,t)
b0_range = np.linspace(B0_min, B0_max, N)
for b0 in b0_range:
    C =run_simulation(b0)
    data = np.insert(data, 0, C, axis=0)   # insert results (rows) in reversed order

# make a 2D surface plot
fig, ax = plt.subplots()
imgplot = ax.imshow(data, interpolation='none', cmap=cm.jet)
cbar = fig.colorbar(imgplot, ticks=[0,0.25, 0.5, 0.75])
cbar.set_label('C, mol/L')
ax.set_xticks([0, N/5, 2*N/5, 3*N/5, 4*N/5, N])
ax.set_xticklabels([0, t_max/5, 2*t_max/5, 3*t_max/5, 4*t_max/5, t_max])
ax.set_xlabel('Reaction time, h')
ax.set_yticks([0, N/2.0, N])
ax.set_yticklabels([B0_max, (B0_max-B0_min)/2.0, B0_min])
ax.set_ylabel('B0, mol/L')
ax.set_title('Fig. 34-1.pdf')
plt.savefig('34-1.pdf')
plt.close()

