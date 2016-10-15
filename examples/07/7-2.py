# File 7-2.py
# Example 7. Solving ODE(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import numpy as np
from scipy.integrate import odeint

def ode(y, t):
    y = y[0]             # unpack variable, it is more convenient write y instead y[0] 
    k = 1.4e-3           # a parameter (just for example)
    dydt = -k*y          # calculate derivative (dy/dt)
    return [dydt]        # return the derivative  

y0 = 2                   # initial conditions y(t0) = 2

t = np.linspace(0,2000,11)             # t goes from 0 to 2000 in steps of 200: (2000-0)/(11-1)
results = odeint(ode, [y0], t)         # do calculations 
y = results[:,0]
print t                                # time ticks
print y                                # and instantaneous y

print t[3]
print y[3]
