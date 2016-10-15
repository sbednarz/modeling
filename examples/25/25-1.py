# File 25-1.py
# Example 25. Concentration profiles
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.misc import derivative

# The reaction: A -> B, k

# Approach 1
# Analytic solution
def analytic(t):
    return A0*np.exp(-k*t)

# Approach 2
# Numerical integration of ODEs
def model(y, t):
    A = y[0]             # unpack variables
    B = y[1]
    dAdt = -k*A          # calculate derivatives
    dBdt = k*A
    return [dAdt, dBdt]  # return derivatives  

# Parameters
k = 1.4e-3               # 1/s
A0 = 2                   # mol/L
B0 = 0

# Time span
t = np.linspace(0, 2000) # 0 - 2000s
# Initial conditions
ic = [A0, B0]

# Calculate concentration vs. time profiles
# analytically
Aa = analytic(t)
# numerically
results = odeint(model, ic, t)
An = results[:,0]

# Compare the results graphically
plt.plot(t, Aa, 'b-', label = 'analytic')
plt.plot(t, An, 'bo', label = 'numeric')
plt.ylabel('[A], mol/L')
plt.xlabel('Time, s')
plt.legend()
plt.title('25-1.pdf')
plt.savefig('25-1.pdf')
plt.close()
