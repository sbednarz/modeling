# File 29-2.py
# Example 29. Second order equilibrium kinetics
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # to solve ODE numerically
from scipy.misc import derivative   # to calculate derivative

# The reaction: 
# 2A -> B, k1
# B -> 2A, k2
def model(y, t):
    A = y[0]                   # unpack variables
    B = y[1]
    dAdt = -2*k1*A*A + 2*k2*B    # calculate derivatives
    dBdt = k1*A*A - k2*B
    return [dAdt, dBdt]  # return derivatives  

# Parameters
k1 = 2e-3                      # 1/s
k2 = 3e-4                      # 1/s
A0 = 2                         # mol/L
B0 = 1                         # mol/L
# Time span
t = np.linspace(0, 6000) # 0 - 6000s
# Initial conditions
ic = [A0, B0]
# Integrate numerically ODEs
results = odeint(model, ic, t)
# Unpack concentrations
A = results[:,0]
B = results[:,1]
# checking the results
# moles balance:
print 2*B+A # should be A0+B0

# Plot the results
plt.plot(t, A, 'bo-', label = 'A')
plt.plot(t, B, 'go-', label = 'B')
plt.ylabel('Conc., mol/L')
plt.xlabel('Time, s')
plt.legend(ncol=2)              # to make the plot nicer
plt.title('29-2.pdf')
plt.savefig('29-2.pdf')
plt.close()

print B[-1]/A[-1]**2

