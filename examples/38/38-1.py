# File 38-1.py
# Example 38. CSTR in series
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Reaction: A -> B, k
# IN -> CSTR1 -> CSTR2 -> OUT
def model(y, t):
    A1 = y[0]
    A2 = y[1]
    dA1dt = F*Ain - F*A1 - V*k*A1
    dA2dt = F*A1 - F*A2 - V*k*A2
    return [dA1dt, dA2dt]

V = 3    # L
F = 0.1   # L/min
k = 0.1   # 1/min
Ain = 2    # mol/L

# simulation time from 0 to 30 min
t = np.linspace(0, 30)
results = odeint(model,[Ain, Ain], t)
A1 = results[:,0]
A2 = results[:,1]
plt.plot(t, A1, 'b-', label='[A] in the reactor 1')
plt.plot(t, A2, 'c--', label='[A] in the reactor 2')
plt.xlabel('Time, min')
plt.ylabel('[A], mol/L')
plt.legend()
plt.title('38-1.pdf')
plt.savefig('38-1.pdf')
plt.close()
