# File 33-1.py
# Example 33. Kinetic model for oxidation process (1)

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
    k2 = 1e-4*3600             # <--- change the value, see the effect (Y & S)
    # ODEs
    dAdt = -k1*A*B
    dBdt = -k1*A*B
    dCdt = k1*A*B - k2*B*C
    dDdt = k2*B*C
    return [dAdt, dBdt, dCdt, dDdt]

A0=1.0
B0=1.5
C0=0
D0=0
ic = [A0, B0, C0, D0]          # initial conditions
t = np.linspace(0,5)
results = odeint( model, ic, t)
A = results[:,0]
B = results[:,1]
C = results[:,2]
D = results[:,3]

alpha = 100*A/A0               # calculate the substrate conversion
Y = 100*C/A0                   # calculate the product yield
S = 100*C/(C+D)                # calculate process selectivity

fig,ax1 = plt.subplots()
ax1.set_title('Fig. 33-1a.pdf')
ax1.plot(t ,A, label='A')
ax1.plot(t ,B, label='B')
ax1.plot(t ,C, label='C')
ax1.plot(t ,D, label='D')
ax1.legend(loc='upper right', ncol=4)
ax1.set_yticks([0,0.5,1.0,1.5])
ax1.set_ylabel('Conc., mol/L')
ax1.set_xlabel('Reaction time, h')
plt.savefig('33-1a.pdf')
plt.close()

fig,ax1 = plt.subplots()
ax1.set_title('Fig. 33-1b.pdf')
ax1.plot(t , alpha, 'b--', label='Conv.A')
ax1.plot(t ,Y, 'g--',  label='Yield C')
ax1.plot(t ,S, 'm--',  label='Sel.C')
ax1.set_xlabel('Reaction time, h')
ax1.set_ylabel('%')
ax1.legend(loc='upper right', ncol=3, handletextpad=0, 
        columnspacing=0.4)
plt.savefig('33-1b.pdf')
plt.close()
