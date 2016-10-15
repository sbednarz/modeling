# File 45-1.py
# Example 45. Exponential and logistic growth
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Exponential growth
def model(y, t):
    N = y[0]
    dNdt = k*N
    return [dNdt]

k = 0.6931 #ln(2)
N0 = 100
t = np.linspace(0, 3)
results = odeint( model, [N0], t)
N = results[:,0]
# doubling time
t2 = np.log(2)/k
str = 'Doubling time = {:.1f} h'.format(t2)

plt.plot(t,N, label='Cells')
plt.xlabel('Time, h')
plt.ylabel('Number')
plt.legend(loc='best')
plt.text(0.5,600,'cells -> more cells')
plt.text(0.5,560,'dN/dt = kN')
plt.text(0.5,520,'autocatalytic process')
plt.text(0.15,295, str)
plt.plot((0,1*t2),(2*N0,2*N0),'k:')
plt.plot((1*t2,1*t2),(N0,2*N0),'k:')
plt.plot((0,2*t2),(4*N0,4*N0),'k:')
plt.plot((2*t2,2*t2),(N0,4*N0),'k:')
plt.savefig('45-1.pdf')
plt.close()
