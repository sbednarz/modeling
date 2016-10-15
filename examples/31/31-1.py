# File 31-1.py
# Example 31. Reversible monomolecular system
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy
from scipy.integrate import odeint

# a = 1-butene, b = cis-2-butene, c = trans-2-butene
def model(y, t):
    a = y[0]
    b = y[1]
    c = y[2]
    #relative rate constants
    k12 = 10.344
    k21 = 4.623
    k31 = 1
    k13 = 3.724
    k23 = 5.616
    k32 = 3.371
    # ODEs
    dadt = -k12*a + k21*b -k13*a + k31*c
    dbdt = k12*a - k21*b + k32*c - k23*b
    dcdt = k13*a - k31*c + k23*b - k32*c
    return [dadt, dbdt, dcdt]

t = numpy.linspace(0, 1) # normalized time
# case 1: pure 1-butene
a0=1
b0=0
c0=0
initial = [a0, b0, c0]
results = odeint( model, initial, t )
# Reagents mole fractions:
a = results[:,0]
b = results[:,1]
c = results[:,2]

fig, ax = plt.subplots()
ax.plot(t, a, 'bo', label='[1-butene]')
ax.plot(t, b, 'ro', label='[cis-2-butene]')
ax.plot(t, c, 'go', label='[trans-2-butene]')
ax.legend()
ax.set_xlabel('Normalized Time')
ax.set_ylabel('Relative Concentations')
fig.savefig('31-1a.pdf')

print('Final (at equilibrium) mole fractions:')
print('A={:.3f} B={:.3f} C={:.3f}'.format(a[-1], b[-1], c[-1]) )
