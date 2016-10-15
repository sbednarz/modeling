# File 30-1.py
# Example 30. Autocatalytic reaction
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # to solve ODE numerically
from scipy.misc import derivative   # to calculate derivative

# The reaction: 
# A + B -> 2B, k1
def model(y, t):
    A = y[0]                     # unpack variables
    B = y[1]
    dAdt = -k1*A*B               # calculate derivatives
    dBdt = k1*A*B
    return [dAdt, dBdt]          # return derivatives  

k1 = 2.16                      # L/molh
A0 = 2                         # mol/L
B0 = 0.0001                    # mol/L, traces of B
t = np.linspace(0, 5) # 0 - 5h
ic = [A0, B0]
results = odeint(model, ic, t)
A = results[:,0]
B = results[:,1]
# calculate reaction rate
rate = k1*A*B
# checking the results - moles balance:
print B+A # should be A0+B0
# Plot the results - 2 plots per graph
fig = plt.figure()
ax1 = plt.subplot(211)
ax1.plot(t, A, 'bo-', label = 'A')
ax1.plot(t, B, 'go-', label = 'B')
ax1.set_ylabel('Conc., mol/L')
ax1.set_xlabel('Time, s')
ax1.legend(ncol=2, loc='center right')  # to make the plot nicer
ax1.set_title('30-1.pdf')
ax2 = plt.subplot(212)
ax2.plot(t, rate, 'ro-')
ax2.set_ylabel('Rate, mol/Lh')
ax2.set_xlabel('Time, s')
ax2.annotate("", xy=(0.02,0.25), xytext=(1.1,0.25), arrowprops=dict(arrowstyle='<->'))
ax2.text(0.6, 0.5, 'Induction\nperiod', horizontalalignment='center')
plt.savefig('30-1.pdf')
plt.close()
