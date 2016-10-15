# File 39-1.py
# Example 39. Isothermal semi-batch reactor
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

# This code is based on LearnChemE example:
# https://www.youtube.com/watch?v=KzMRcACcvsA

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# A -> C rA = -k*CA*CB
def model(y,t):
    # unpack instantaneous values
    nA = y[0]
    nB = y[1]
    nC = y[2]
    V = y[3]
    # calculate instant concentrations
    A=nA/V
    B=nB/V
    C=nC/V
    # derivative mole balances
    dnAdt = -k*A*B*V
    dnBdt = FB                          # molar flow rate (mol/min) of B
    dnCdt = k*A*B*V                     # 
    dVdt = v                            # flow rate of the catalyst addition
    return [dnAdt, dnBdt, dnCdt, dVdt]

nA0 = 54000                             # moles
nB0 = 0 
nC0 = 0
V0 = 2700                               # L
k=0.25                                  # L/(mol min)
FB= 0.05 * 12.5                         # mol/min
v=12.5                                  # L/min 

ic = [nA0, nB0, nC0, V0]                # initial conditions
t = np.linspace(0,200)                  # 0 - 200 min
results = odeint(model, ic, t)

# results post-processing
nA = results[:,0]
nB = results[:,1]
nC = results[:,2]
V = results[:,3]
A = nA/V
B = nB/V
C = nC/V
print "Final number of moles of C (after 200min) = {:.0f} mole".format(nC[-1]) 
# -1 means the last element == 200min
print "Final concentration of C (after 200min) = {:.0f} mol/L".format(C[-1])

plt.subplot(311)
plt.plot(t,A, 'g-', label='[A]')
plt.plot(t,C, 'c-', label='[C]')
plt.xticks([0, 50, 100, 150, 200],[])
plt.legend(loc='upper right', ncol=2)

plt.subplot(312)
plt.plot(t,B, 'm-', label='[B]')
plt.xticks([0, 50, 100, 150, 200],[])
plt.yticks([0, 0.015, 0.030])
plt.legend(loc='upper left')

plt.subplot(313)
plt.plot(t,V, 'b-', label='V, L')
plt.xlabel('Time, min')
plt.yticks([2500, 3500, 4500, 5500])
plt.legend(loc='upper left')
plt.savefig('39-1.pdf')
plt.close()
