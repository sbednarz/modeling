# File 41-1.py
# Example 41. Heat balance - filling a tank
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def model(y, t):
    m = y[0]                    # mass at instant time
    T = y[1]                    # temperature at instant time
    dmdt = F1*rho               # mass balance

                                # See Newton's law of cooling
    dTdt = F1*rho*(T1-T)/m      # T1-T is time-dependent thermal gradient 
                                # between hot stream and water inside the tank.
                                # Heat capacity of the inlet steam is equal 
                                # to h.c. of the mixture in the tank, therefore is shortened
    return [dmdt, dTdt]

# hot stream
F1 = 0.1        # m3/h
rho = 1000      # kg/m3
T1 = 60         #degC
# initial conditions
m0 = 20 # kg
T0 = 20 # degC

t = np.linspace(0, 1) # 0-1h
results = odeint(model, [m0, T0], t)

m = results[:,0]
T = results[:,1]
plt.plot(t,m,label='m, kg')
plt.plot(t,T,label='T, degC')
plt.xlabel('Filling time, h')
plt.legend(loc='best')
plt.savefig('41-1.pdf')
plt.close()

# checking the calculations
cp = 4.18    # kJ/(kg K), average mass-specific heat capacity of water
Te = T[-1]   # final temperature of water in the tank
me = m[-1]   # final mass of water in the tank
m1 = me-m0   # mass of water feeded
print "Checking ..."
print "Q initial (J) + Q introduced (J)"
print cp*m0*(T0) + cp*m1*(T1)
print "Q total (J)"
print cp*me*Te
