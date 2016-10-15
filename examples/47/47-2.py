# File 47-2.py
# Example 47. Fermentation - Monod model
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Fermentation (Monod growth kinetics)
def model(y, t):
    X = y[0]
    S = y[1]
    P = y[2]
    mi = mi_max * S/(KM + S)
    dXdt = X * mi
    dSdt = -1/Y_XS * X * mi
    dPdt = Y_PX * X * mi
    return [dXdt, dSdt, dPdt]

KM = 0.4 # g/L
Y_XS = 0.5
Y_PX = 0.1
mi_max = 1 # 1/h

# initial conditions
X0 = 0.1 # g/L
S0 = 10  # g/L
P0 = 0   # g/L

t = np.linspace(0, 5) # 0-5h
results = odeint( model, [X0, S0, P0], t)
X = results[:,0]
S = results[:,1]
P = results[:,2]

# calculate rates
dXdt = mi_max * X * S/(KM + S)
dSdt = -1/Y_XS * mi_max * X * S/(KM + S) # minus = uptake
dPdt = Y_PX * mi_max * X * S/(KM + S)

plt.plot(t,dXdt, label='dXdt')
plt.plot(t,dSdt, label='dSdt')
plt.plot(t,dPdt, label='dPdt')
plt.xlabel('Time, h')
plt.ylabel('Rate, g/Lh')
plt.legend(loc='best')
plt.title('47-2.pdf')
plt.savefig('47-2.pdf')
plt.close()

# yield coefficients
print 'dXdt/-dSdt'
print dXdt/-dSdt
print 'dPdt/dXdt'
print dPdt/dXdt

# Mass balances
print S + X + P
