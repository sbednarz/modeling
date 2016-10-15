# File 28-2.py
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
rate = k1*A - k2*B 

# Plot the results
plt.plot(t, rate, 'mo')
plt.ylabel('Reaction rate, mol/(Ls)')
plt.xlabel('Time, min')
plt.title('28-2.pdf')
plt.savefig('28-2.pdf')
plt.close()
