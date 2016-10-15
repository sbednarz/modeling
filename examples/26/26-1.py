# File 26-1.py
# Example 26. Rate of reaction
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # to solve ODE numerically
from scipy.misc import derivative   # to calculate derivative

# The reaction: A -> B, k

# Approach 1
# Analytic solution (possible only for relatively simple mechanisms)
def analytic(t):
    return A0*np.exp(-k*t)

# Approach 2
# Numerical integration of ODEs
def model(y, t):
    A = y[0]             # unpack variables
    B = y[1]
    dAdt = -k*A          # calculate derivatives
    dBdt = k*B
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

# Let's calculate the reaction rates
# r= -dA/dt = k*A so
rdef = k*Aa # or k*An
# or calculate derivatives numerically
rderiv = -derivative(analytic, t)

# We can calculate the rate at different reaction time 
# special meaning have the initial rate (at t=0)
# Let's calculate - numerically
r0 = -derivative(analytic, 0)
print("Initial rate (derivative):")
print(r0)
# or from the rate definition
# note that at t=0 A=A0
r00 = k*A0
print("Initial rate (def):")
print(r00)
# or based on derivative approximation
print("Initial rate (approximation):")
r0aprox = -(Aa[1] - Aa[0])/(t[1] - t[0])
print(r0aprox)

# Compare the results
plt.plot(t, rdef, 'g-', label = 'analytic')
plt.plot(t, rderiv, 'go', label = 'numeric')
plt.ylabel('Rate, mol/(Ls)')
plt.xlabel('Time, s')
plt.legend()
plt.title('26-1.pdf')
plt.subplots_adjust(left=0.2,right=0.9) # to make plot more clear
plt.savefig('26-1.pdf')
plt.close()
