# File 28-1.py
# Example 28. First order equilibrium kinetics
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # to solve ODE numerically
from scipy.misc import derivative   # to calculate derivative

# The reaction: 
# A -> B, k1
# B -> A, k2
def model(y, t):
    A = y[0]                   # unpack variables
    B = y[1]
    dAdt = -k1*A + k2*B        # calculate derivatives
    dBdt = k1*A - k2*B
    return [dAdt, dBdt]  # return derivatives  

# Parameters
k1 = 1e-3*60                   # 1/min
k2 = 2e-4*60                   # 1/min
A0 = 2                         # mol/L
B0 = 0                         # mol/L
# Time span
t = np.linspace(0, 60) # 0 - 60min
# Initial conditions
ic = [A0, B0]
# Integrate numerically ODEs
results = odeint(model, ic, t)
# Unpack concentrations
A = results[:,0]
B = results[:,1]
# checking the results
# moles balance:
print "Moles balance: B+A:"
print B+A # should be A0+B0

# Plot the results
plt.plot(t, A, 'bo', label = 'A')
plt.plot(t, B, 'go', label = 'B')
plt.ylabel('Conc., mol/L')
plt.xlabel('Time, min')
plt.legend(ncol=2)              # to make the plot nicer
plt.title('28-1.pdf')
plt.savefig('28-1.pdf')
plt.close()

# print final concentrations (at equilibrium)
print "A_eq: {:.2f} mol/L".format(A[-1])
print "B_eq: {:.2f} mol/L".format(B[-1])

