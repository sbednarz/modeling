# File 31-a.py
# Example 31. Reversible monomolecular system
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt

import numpy
from scipy.integrate import odeint


# Wei 1962
# a = 1-butene
# b = cis-2-butene
# c = trans-2-butene


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

    dadt = -k12*a + k21*b -k13*a + k31*c
    dbdt = k12*a - k21*b + k32*c - k23*b
    dcdt = k13*a - k31*c + k23*b - k32*c
    return [dadt, dbdt, dcdt]

t = numpy.linspace(0, 1) # ts => time

# set 1
a0=1
b0=0
c0=0
initial = [a0, b0, c0]
res1 = odeint( model, initial, t )

# set 2
a0=0
b0=1
c0=0
initial = [a0, b0, c0]
res2 = odeint( model, initial, t )

# set 3
a0=0
b0=0
c0=1
initial = [a0, b0, c0]
res3 = odeint( model, initial, t )



fig, ax = plt.subplots()
ax.plot(t, res1[:,0], 'bo', label='[1-butene]')
ax.plot(t, res1[:,1], 'ro', label='[cis-2-butene]')
ax.plot(t, res1[:,2], 'go', label='[trans-2-butene]')
ax.legend()
ax.set_xlabel('Normalized Time')
ax.set_ylabel('Relative Concentations')
fig.savefig('31-1a.pdf')

fig, ax = plt.subplots()
ax.plot(t, res2[:,0], 'bo', label='[1-butene]')
ax.plot(t, res2[:,1], 'ro', label='[cis-2-butene]')
ax.plot(t, res2[:,2], 'go', label='[trans-2-butene]')
ax.legend()
ax.set_xlabel('Normalized Time')
ax.set_ylabel('Relative Concentations')
fig.savefig('31-1b.pdf')

fig, ax = plt.subplots()
ax.plot(t, res3[:,0], 'bo', label='[1-butene]')
ax.plot(t, res3[:,1], 'ro', label='[cis-2-butene]')
ax.plot(t, res3[:,2], 'go', label='[trans-2-butene]')
ax.legend()
ax.set_xlabel('Normalized Time')
ax.set_ylabel('Relative Concentations')
fig.savefig('31-1c.pdf')



#for i in range(0,t.size):
#	print a[i], b[i], c[i]


