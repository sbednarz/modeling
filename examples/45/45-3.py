# File 45-3.py
# Example 45. Exponential and logistic growth
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Logistic model
def model(y, t):
    P = y[0]
    dPdt = r*P * (1-P/C)
    return [dPdt]

# growth rate
r = 1
# carrying capacity
C = 130.0
# initial population
P0 = 1
# simulation time
t_min = 0
t_max = 10

t = np.linspace(t_min, t_max)
results = odeint( model, [P0], t)
P = results[:,0]
dPdt = r*P * (1-P/C)
plt.plot(t,dPdt, 'c-')
plt.xlabel('Time')
plt.ylabel('Population growth rate, dP/dt')
plt.legend(loc='best')
plt.savefig('45-3.pdf')
plt.close()
