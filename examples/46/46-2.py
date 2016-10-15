# File 46-2.py
# Example 46. Monod growth
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Monod growth
def model(y, t):
    X = y[0]
    S = y[1]
    mi = mi_max*S/(KM+S)     # the specific growth rate
    dXdt = X * mi            # biomass growth rate
    dSdt = -1/Y * X * mi     # limiting substrate consumption rate
    return [dXdt, dSdt]

mi_max = 0.0382 # the maximum specific growth rate of the cells
KM = 6 # the saturation constant
Y = 0.139e-3 # The yield coefficients

# Initial conditions
X0 = 0.002  # O.D.
S0 = 200    # nitrite ug/ml 

# Fermentation simulation
t = np.linspace(0, 100)
results = odeint( model, [X0, S0], t)
X = results[:,0]
S = results[:,1]
# Calculation the rates
dXdt = X * mi_max*S/(KM+S)
dSdt = 1/Y * X * mi_max*S/(KM+S)

ax = plt.subplot(211)
ax.set_title('46-2.pdf')
ax.plot(t, dXdt, 'g-', label='dXdt')
ax.set_xlabel('Time, h')
ax.set_ylabel('Rate')
ax.legend(loc='upper left')
ax = plt.subplot(212)
ax.plot(t, dSdt, 'b-',label='dSdt')
ax.set_xlabel('Time, h')
ax.set_ylabel('Rate')
ax.legend(loc='upper left')
plt.subplots_adjust(left=0.2, right=0.9)
plt.savefig('46-2.pdf')
plt.close()

print 'dXdt/dSdt = '
print dXdt/dSdt
print('Y = {}'.format(Y))

