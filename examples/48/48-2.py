# File 48-2.py
# Example 48. Batch Alcoholic Fermentation
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Model B, see:
# F. Gbdia, C. Casas and C. Sola
# Chem. Tech. Biorechnol. 1988,41, 155-165

def modelB(y, t):
    X = y[0]
    P = y[1]
    S = y[2]
    dXdt = mi_0 * X * (S/(KS + S)) * (KP/(KP + P)) - KD*X
    dPdt = ni_max * X * (S/(KSS + S)) * (KPP/(KPP + P))
    dSdt = -1/RSX * dXdt - 1/RSP*dPdt
    return [dXdt, dPdt, dSdt]

mi_0 = 0.522 # 1/h
KS = 0.210 # g/L
KP = 2.42 # g/L
KD = 0.0078
ni_max = 1.36 # 1/h
KSS = 1.68 # g/L
KPP = 7.29 # g/L
RSX = 0.299
RSP = 0.448

X0 = 0.002 # g d.w./L
P0 = 0.0 #
S0 = 75.0 # g/L

t = np.linspace(0, 60)
results = odeint( modelB, [X0, P0, S0], t)
X = results[:,0]
P = results[:,1]
S = results[:,2]


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(t,X, 'g', label='X')
ax1.set_ylabel('Yeast conc. (X), g d.w./L')
ax1.legend(loc='upper right')
#ax1.set_ylim(0,5)
ax2 = ax1.twinx()
ax2.plot(t,S, 'y', label='S')
ax2.plot(t,P, 'b', label='P')
ax2.set_ylabel('Glucose, ethanol , g/L')
ax2.set_xlabel('Time, h')
ax2.legend(loc='upper left')
plt.title('48-2.pdf')
plt.savefig('48-2.pdf')
plt.close()
