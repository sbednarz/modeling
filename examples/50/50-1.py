# File 50-1.py
# Example 50. Chemostat
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

# algebraic equations
def steadystate(y):
    X = y[0]
    S = y[1]
    P = y[2]
    mi = mi_max * S/(KM + S)
    rX = X * mi
    rS = -1/Y_XS * X * mi
    rP = Y_PX * X * mi
    eq1 = rX - D*X
    eq2 = D*Sf - D*S + rS
    eq3 = rP - D*P
    return [eq1, eq2, eq3]

def Dmax(S0):
     return mi_max * S0/(KM + S0)

# ODEs
def model(y, t):
    X = y[0]
    S = y[1]
    P = y[2]
    mi = mi_max * S/(KM + S)
    rX = X * mi
    rS = -1/Y_XS * X * mi       # note negative value
    rP = Y_PX * X * mi
    # non-steady state
    dXdt = rX - D*X             # sterile feed
    dSdt = D*Sf - D*S + rS      # +rS because rS is negative, see above 
    dPdt = rP - D*P
    return [dXdt, dSdt, dPdt]

Sf = 5 # g/L
D = 0.1 # 1/h     <----------------- try values from 0.01 to 1
KM = 0.4 # g/L
Y_XS = 0.5
Y_PX = 0.1
mi_max = 0.8 # 1/h


X0 = 0.1 # g/L
S0 = Sf  # g/L
P0 = 0   # g/L
 

tmax = 50 # h 
t = np.linspace(0, tmax) 
results = odeint( model, [X0, S0, P0], t)
X = results[:,0]
S = results[:,1]
P = results[:,2]

# calculation of steady state concentrations
guess = [2,0,0.1]
ss = fsolve(steadystate, guess)
Xss = ss[0]
Sss = ss[1]
Pss = ss[2]

#print Dmax(S0)
#print Xss, Sss, Pss

fig = plt.figure()
fig.subplots_adjust(hspace = 0.5, left=0.2, right=0.7)
ax = fig.add_subplot(311)
ax.set_title('50-1.pdf')
ax.plot(t, X, 'g-')
ax.set_xticks([])
ax.locator_params(axis = 'y',tight=False, nbins=3)
ax = fig.add_subplot(312)
ax.plot(t, S, 'b')
ax.set_xticks([])
ax.locator_params(axis = 'y',tight=False, nbins=3)
ax = fig.add_subplot(313)
ax.plot(t, P, 'y')
ax.locator_params(axis = 'y',tight=False, nbins=3)
ax.set_xlabel('Fermentation time, h')

ax.text(0.01,0.9,'X, g/L', transform=fig.transFigure)
ax.text(0.01,0.62,'S, g/L', transform=fig.transFigure)
ax.text(0.01,0.35,'P, g/L', transform=fig.transFigure)

ax.text(0.73,0.9, 'X0={:.3f} g/L'.format(X0) , transform=fig.transFigure)
ax.text(0.73,0.84, 'S0={:.3f} g/L'.format(S0) , transform=fig.transFigure)
ax.text(0.73,0.78, 'D={:.3f} 1/h'.format(D) , transform=fig.transFigure)
ax.text(0.73,0.66, 'Dmax={:.3f} 1/h'.format(Dmax(S0)) , transform=fig.transFigure)

if D < Dmax(S0):
    ax.text(0.73,0.60, 'At steady state:' , transform=fig.transFigure)
else:
    ax.text(0.73,0.60, '! Washout:' , transform=fig.transFigure)

ax.text(0.73,0.54, 'X={:.3f} g/L'.format(Xss) , transform=fig.transFigure)
ax.text(0.73,0.48, 'S={:.3f} g/L'.format(Sss) , transform=fig.transFigure)
ax.text(0.73,0.42, 'P={:.3f} g/L'.format(Pss) , transform=fig.transFigure)
ax.text(0.73,0.36, 'D*X={:.3f} g/(L h)'.format(D*Xss) , transform=fig.transFigure)
ax.text(0.73,0.30, 'conv.S={:.1f}%'.format(100*(S0-Sss)/S0) , transform=fig.transFigure)
ax.text(0.73,0.24, 'D*P={:.3f} g/(L h)'.format(D*Pss) , transform=fig.transFigure)
plt.savefig('50-1.pdf')
plt.close()

