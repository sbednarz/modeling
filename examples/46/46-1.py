# File 46-1.py
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
    dXdt = X * mi            # biomass growth (e.g. nitrobacter cells)
    dSdt = -1/Y * X * mi     # limiting substrate uptake
    return [dXdt, dSdt]

mi_max = 0.0382 # the maximum specific growth rate of the cells
KM = 6 # the saturation constant
Y = 0.139e-3 # The yield coefficients

# Initial conditions
X0 = 0.002  # O.D.
S0 = 200    # nitrite ug/ml 

# specific growth rate
S = np.linspace(0,200) # substrate concentration
mi = mi_max*S/(KM+S)   # the rate
plt.plot(S, mi)
plt.xlabel('S0, $\mu$g/mL')
plt.ylabel('Specific growth rate, $\mu$')
plt.title('46-1a.pdf')
plt.savefig('46-1a.pdf')
plt.close()

# Fermentation simulation
t = np.linspace(0, 100)
results = odeint( model, [X0, S0], t)
X = results[:,0]
S = results[:,1]
ax1 = plt.subplot(111)
ax1.plot(t,X, 'g', label='X')
ax1.set_ylabel('Cell conc. (X), UOD')
ax1.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.plot(t,S, 'y', label='S')
ax2.set_ylabel('NO2- (S), ul/ml')
ax2.set_xlabel('Time, h')
ax2.legend(loc='upper right')
plt.title('46-1b.pdf')
plt.savefig('46-1b.pdf')
plt.close()
