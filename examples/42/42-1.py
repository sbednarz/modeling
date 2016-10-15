# File 42-1.py
# Example 42. Heat generation
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# kinetic model
def rA(A):
    k = 0.65 # 1/min
    return -k*A

def model(y, t):
    A = y[0]
    Q = y[1]
    dAdt = rA(A)           # component A balance
    dQdt = dAdt*V0*H       # instantaneous heat release rate
    return [dAdt, dQdt]

A0 = 2.0 # mol/L
H = -125.574 #kJ/mol
V0 = 10 # L

ic = [A0, 0]               # initial conditions: A0, Q0
Qmax = -A0*V0*H            # <---
t = np.linspace(0,5)       # 0 - 5 min
results = odeint(model, ic, t)
A = results[:,0]
Q = results[:,1]

alpha = (A0-A)/A0          # calculate conversion of A
dAdt = rA(A)               # rate of reaction
q = dAdt*V0*H              # instantaneous heat release rate (kJ/min) 

plt.subplots_adjust(hspace = 0.5, left=0.2, right=0.9)
plt.subplot(211)
plt.plot(t, alpha, label='Conversion - A')
plt.legend(loc='best')
plt.xticks([])
plt.ylabel('Conversion')
plt.subplot(212)
plt.plot(t, Q, 'r-', label='Q')
plt.plot((0,5),(Qmax, Qmax), 'r:', label='Qmax')
plt.legend(loc='best', ncol=2)
plt.xlabel('Time, min')
plt.ylabel('Heat (Q), kJ')
plt.savefig('42-1a.pdf')
plt.close()

plt.subplots_adjust(hspace = 0.5, left=0.2, right=0.9)
plt.subplot(211)
plt.plot(t, -dAdt, 'b--', label='dAdt')
plt.legend(loc='best')
plt.xticks([])
plt.ylabel('Rate, mol/(L min)')
plt.subplot(212)
plt.plot(t, q, 'r--', label='q')
plt.legend(loc='best')
plt.xlabel('Time, min')
plt.ylabel('q, kJ/min')
plt.ylim(0,2000)
plt.savefig('42-1b.pdf')
plt.close()
