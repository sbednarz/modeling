# File 16-1.py
# Example 16. Equilibrium composition - gas phase reactions
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve

def model(vars):
	x = vars[0]    # equilibrium number of moles of CH3Cl
	y = vars[1]    # equilibrium number of moles of the ether (ch3_2o)
	Kp1 = 0.00154
	Kp2 = 10.6
	eq1 = ((x-2*y)/n0 * x/n0)/((1-x)/n0 * (1-x+y)/n0) - Kp1
	eq2 = (y/n0 * (1-x+y)/n0)/((x-2*y)/n0)**2 - Kp2
	return [eq1, eq2]


# we assume total mole number of 2 (molar ratio 1:1)
n0 = 2
# try different guess values ranged from 1e-5 to 1e-2
ini = [1e-3,1e-3]
# main calculations
x,y = fsolve(model, ini)
# report ....
print('x={:.2e} y={:.2e}'.format(x, y))

# Validation of the solution
# Calculations of number of moles
n_ch3cl = 1-x
n_h2o = 1-x+y
n_ch3oh = x-2*y     # this expression could be a bit difficult to understand 
n_hcl = x
n_ch3_2o = y
# Molar fractions
y_ch3cl = (1-x)/n0
y_h2o = (1-x+y)/n0
y_ch3oh = (x-2*y)/n0
y_hcl = x/n0
y_ch3_2o = y/n0
# reporting
print("y_ch3cl = {:.3e}".format(y_ch3cl))
print("y_h2o = {:.3e}".format(y_h2o))
print("y_ch3oh = {:.3e}".format(y_ch3oh))
print("y_hcl = {:.3e}".format(y_hcl))
print("y_ether = {:.3e}".format(y_ch3_2o))

# Element balance
print("Chlorine balance (1mol)")
print n_ch3cl + n_hcl
print("Carbon balance (1mol)")
print n_ch3cl + n_ch3oh + 2*n_ch3_2o
print("Oxygen balance (1mol)")
print n_h2o + n_ch3oh + n_ch3_2o
print("Hydrogen balance (5mol)")
print 3*n_ch3cl + 2*n_h2o + 4*n_ch3oh + 1*n_hcl + 6*n_ch3_2o
# final checking
Kp1calc = (y_ch3oh*y_hcl)/(y_ch3cl*y_h2o)
Kp2calc = (y_ch3_2o*y_h2o)/y_ch3oh**2
print("Calculated Kp1 = {:.2e}".format(Kp1calc))
print("Calculated Kp2 = {:.2e}".format(Kp2calc))
