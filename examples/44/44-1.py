# File 44-1.py
# Example 44. Adiabatic batch reactor
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# calculate the rate at an instant of concentration (A) and temperature (T) 
def rA(A, T):
    k = 0.0025*np.exp(-1760/T)
    return k*A**2.5

# ODEs
def model(y, t):
    A = y[0]                           # instant concentration of A
    T = y[1]                           # instant temperature
    dAdt = -rA(A, T)                   # calculate the rate at time t and at temperature T
    dTdt = -rA(A, T)*delH / (A0*cpA)   # rate of change of temperature (from heat balance)
    return [dAdt, dTdt]

delH = -14600  # kJ/mol
cpA = 83.6     # J/(mol K)
A0 = 5.0       # mol/L
T0 = 373       # K

t = np.linspace(0, 4000)               # 0-4000s
results = odeint(model, [A0, T0], t)
A = results[:,0]                       # A(t)
T = results[:,1] - 273                 # extract temperature & convert it from K to degC
X = (A0-A)/A0                          # calculate conversion from A(t)

plt.subplots_adjust(hspace = 0.5, left=0.2, right=0.9) # just to make the plot more clear
plt.subplot(211)
plt.plot(t/60.0, X, 'bo-')             # t/60.0 => convert time unit from s to min
plt.plot((0, 70), (0.6, 0.6),'k:')
plt.ylabel('[A], mol/L')
plt.subplot(212)
plt.plot(t/60.0, T, 'ro-')
plt.xlabel('Time, min')
plt.ylabel('Temperature, degC')
plt.savefig('44-1.pdf')
plt.close()
