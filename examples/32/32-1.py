# File 32-1.py
# Example 32. Fractional order reactions
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#empirical rate expression 1
def rI(I,M):
    k1 = 5e-4
    a1 = 0.9
    b1 = 0.7
    return -k1 * I**a1 * M**b1

#empirical rate expression 2
def rM(I,M):
    k2 = 1e-3
    a2 = 0.5
    b2 = 1.3
    return -k2 * I**a2 * M**b2

# ODEs
def model(y, t):
    I = y[0]
    M = y[1]
    dIdt = rI(I,M)
    dMdt = rM(I,M)   
    return [dIdt, dMdt]

# initial conditions:
I0 = 0.5 # mol/L
M0 = 2.5 # mol/L

t = np.linspace(0,4000)
results = odeint(model, [I0, M0], t)
I = results[:,0]
M = results[:,1]
dIdt = rI(I,M)
dMdt = rI(I,M)
plt.plot(t, I, 'c-', label='[I]')
plt.plot(t, M, 'b:', label='[M]')
plt.legend(loc='best')
plt.xlabel('Time, s')
plt.ylabel('Conc., mol/L')
plt.title('1.pdf')
plt.savefig('32-1a.pdf')
plt.close()
plt.subplots_adjust(left=0.25, right=0.9)
plt.plot(t, -dIdt, 'c-', label='[I]')      # to have positive rate
plt.plot(t, -dMdt, 'b:', label='[M]')
plt.legend(loc='upper right')
plt.xlabel('Time, s')
plt.ylabel('Rate, mol/Ls')
plt.title('32-1b.pdf')
plt.savefig('32-1b.pdf')
