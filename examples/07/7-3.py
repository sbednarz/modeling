# File 7-3.py
# Example 7. Solving ODE(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def model(y, t):
    A = y[0]             # unpack variables
    B = y[1]
    dAdt = -k*A          # calculate derivatives
    dBdt = k*A
    return [dAdt, dBdt]  # return derivatives  

# Parameters
# They can be inside a ODEs function or outside 
k = 1.4e-3
A0 = 2               
B0 = 0

# Time span
t = np.linspace(0, 2000, 11) # 0 - 2000 step 200
# Initial conditions
ic = [A0, B0]

results = odeint(model, ic, t)
A = results[:,0]
B = results[:,1]

# print the results
print t
print A
print B
print
# or in a more clear form:
print "idx\tt\t\tA\t\tB"
for i in range(t.size):
    print "{}\t{}\t\t{:.3f}\t\t{:.3f}".format(i,t[i], A[i], B[i])

# and plotting the results
plt.plot(t, A, 'bo-', label = 'A')
plt.plot(t, B, 'go-', label = 'B')
plt.ylabel('A, B, a.u.')
plt.xlabel('t, a.u.')
plt.legend(loc='best')
plt.title('7-2.pdf')
plt.savefig('7-2.pdf')
plt.close() 
