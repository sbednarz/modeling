# File 6-5.py
# Example 6. Solving algebraic equation(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def system( unknowns ):
    x = unknowns[0]       # unpack x
    y = unknowns[1]       # unpack y
    eq1 = y - x**2 - 2*x       # calculate eq1 for given x,y
    eq2 = y - 12 + x**2    # calculate eq2 for given x,y
    return [eq1, eq2]     # return the results (0?)

guess = [1, 1]
x0, y0 = fsolve(system, guess)
guess = [-10, -10]
x1, y1 = fsolve(system, guess)

x = np.linspace(-4, 4)
plt.plot(x, x**2 + 2*x, 'b-')
plt.plot(x, 12-x**2, 'c-')

plt.plot((-4,x0), (y0,y0),'k:')
plt.plot((x0,x0), (y0,-5),'k:')

plt.plot((-4,x1), (y1,y1),'k:')
plt.plot((x1,x1), (y1,-5),'k:')

plt.plot(x0,y0,'yD')
plt.plot(x1,y1,'gD')

plt.text(-1,-3,'$y=x^2+2x$')
plt.text(-1,13,'$y=12-x^2$')

plt.text(-5,y0,'$y_0$')
plt.text(-5,y1,'$y_1$')
plt.text(x0,-9,'$x_0$')
plt.text(x1,-9,'$x_1$')


plt.savefig('6-5.pdf')
plt.close()

