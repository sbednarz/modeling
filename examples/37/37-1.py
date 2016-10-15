# File 37-1.py
# Example 37. Reaching steady state in CSTR
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from __future__ import division
import matplotlib.pyplot as plt
import matplotlib.patches as p
import numpy as np
from scipy.integrate import odeint

# Reaction: 2A -> B, k
# Reaching steady state in a CSTR
def model(y, t):
    A = y[0]
    r = 2*k*A**2
    dAdt = F*Af - F*A - r*V
    return [dAdt]

V = 10    # L
F = 0.1   # L/min
k = 0.04   # 1/min
Af = 2    # mol/L

# simulation time from 0 to 30 min
t = np.linspace(0, 30)

# case 1. Initially reactor filled with an inert
A0 = 0
results = odeint(model, [A0], t)
A1 = results[:,0]

# case 2. Initially reactor filled with feed
A0 = 2 # mol/L
results = odeint(model,[A0], t)
A2 = results[:,0]
Afinal = A1[-1]
txt = "Steady state [A]={:.2f} mol/L".format(Afinal)

# Plot
ax = plt.subplot()
ax.plot(t, A1, 'b-', label='[A]0 = 0 mol/L')
ax.plot(t, A2, 'c--', label='[A]0 = 2 mol/L')
ax.set_xlabel('Time, min')
ax.set_ylabel('[A], mol/L')
ax.annotate('', xy=(5,0.49), xytext=(29.8,0.49), arrowprops=dict(arrowstyle='<->'))
ax.text(9, 0.52,txt)
ax.legend()

# Reactor scheme
ax.add_patch(p.Arrow(3,1.1,3,0, width=0.05, facecolor='black'))
ax.add_patch(p.Arrow(11,1.1,3,0, width=0.05, facecolor='black'))
ax.add_patch(p.Rectangle((6,0.7),5,0.7,fill=False))
ax.add_patch(p.Rectangle((6,0.7),5,0.4,facecolor='#eeeeee'))
ax.text(7.5,1.5,'CSTR')
ax.text(8.2,0.85,'V')
ax.text(1.5,1.2,'F,[A]0')
ax.text(12,1.2,'F,[A]')
plt.savefig('37-1.pdf')
plt.close()


