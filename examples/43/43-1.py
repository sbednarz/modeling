# File 43-1.py
# Example 43. Non isothermal kinetics
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def model(y, t):
   A = y[0]
   T = y[1]
   k = k0*np.exp(-Ea/(R*T))  # calculate instant k at T
   dAdt = -k*A               # A -> B ; da/dt = ka; kinetic model
   dTdt = rT                 # heating/cooling rate
   return [dAdt, dTdt]

# The model parameters
R = 8.314e-3                 # kJ/mol*K
# Activation energy
Ea = 78                      # kJ/mol
# Preexponential factor
k0 = 10**11.0                # L/mol*s
# Calculation time: 0 - 300s
t_range = np.linspace(0, 300)

# Initial conditions
A0 = 2          # mol/L
T0 = 310        # K
ic = [A0, T0]   # initial conditions         

# Case 1
# dT/dt = 0 isothermal
rT = 0
results = odeint(model, ic, t_range)
A1 = results[:,0]
T1 = results[:,1]

# Case 2
# dT/dt = 0.066 deg/s linear heating
rT = 20/300.0
results = odeint(model, ic, t_range)
A2 = results[:,0]
T2 = results[:,1]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t_range, A1, 'g-')
ax2.plot(t_range, T1, 'b-')
ax1.set_ylim(0,2)
ax1.set_xlabel('Time, s')
ax1.set_ylabel('[A], mol/L', color='g')
ax2.set_ylabel('Temperature, K', color='b')
plt.title('Fig. 43-1a.pdf')
plt.savefig('43-1a.pdf')
plt.close()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(t_range, A2, 'g-')
ax2.plot(t_range, T2, 'b-')
ax1.set_xlabel('Time, s')
ax1.set_ylabel('[A], mol/L', color='g')
ax2.set_ylabel('Temperature, K', color='b')
plt.title('Fig. 43-1b.pdf')
plt.savefig('43-1b.pdf')
plt.close()
