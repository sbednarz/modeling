# File 7-1.py
# Example 7. Solving ODE(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import numpy as np
from scipy.integrate import odeint

def ode(y, t):
    y = y[0]             # unpack variable, it is more convenient write y instead y[0] 
    k = 1.4e-3           # a parameter (just for example)
    dydt = -k*y          # calculate derivative (dy/dt)
    
    # just to show calculations progress
    print "tn={:.5f}\tyn={:.5f}\tdydt(tn, yn)={:.5f}".format(t,y,dydt)

    return [dydt]        # return the derivative value  


t0 = 0                   # initial time
y0 = 2                   # initial conditions: y(t0) = 2
t1 = 18                  # we are interested in the value of y at t1 = 18 

print "Calculations done by odeint():"
results = odeint(ode, [y0], [t0, t1])  # integrate the ODE
y = results[:,0]                       # results is two-elements vector
print "Raw results: ", y
print "Initial conditions t=0 and y={}".format(y[0]) # element '0'
print "The solution for t=18: y={}".format(y[1])   # element '1'
