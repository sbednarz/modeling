# File 27-1.py
# Example 27. Second order kinetics
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # to solve ODE numerically
from scipy.misc import derivative   # to calculate derivative

# The reaction: A + B -> C, k

def model(y, t):
    A = y[0]                   # unpack variables
    B = y[1]
    C = y[2]
    dAdt = -k*A*B              # calculate derivatives
    dBdt = -k*A*B
    dCdt = k*A*B
    return [dAdt, dBdt, dCdt]  # return derivatives  

# Parameters
k = 3e-3                       # L/(mol s)
A0 = 2                         # mol/L
B0 = 1                         # mol/L
C0 = 0                         # mol/L

# Time span
t = np.linspace(0, 1200) # 0 - 1200s
# Initial conditions
ic = [A0, B0, C0]

# Integrate numerically ODEs
results = odeint(model, ic, t)
# Unpack concentrations
A = results[:,0]
B = results[:,1]
C = results[:,2]

# checking the results
# moles balance:
print C+A # should be A0
print C+B # should be B0


# Plot the results
plt.plot(t, A, 'bo', label = 'A')
plt.plot(t, B, 'go', label = 'B')
plt.plot(t, C, 'yo', label = 'C')
plt.ylabel('Conc., mol/L')
plt.xlabel('Time, s')
plt.legend()
plt.title('27-1.pdf')
plt.savefig('27-1.pdf')
plt.close()
