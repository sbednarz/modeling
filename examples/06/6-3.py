# File 6-3.py
# Example 6. Solving algebraic equation(s)
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def equation(x):
    eq =  x**3 - 2*x**2 - 9*x + 10
    return eq

guess = 6
x1, = fsolve(equation, guess)
guess = 0
x2, = fsolve(equation, guess)
guess = -10
x3, = fsolve(equation, guess)

x = np.linspace(-4,6)
plt.plot(x, equation(x), 'k-')
plt.plot((-4,6), (0,0), 'k:')
plt.plot((0,0), (-60,100), 'k:')
plt.plot(x1,0,'rD')
plt.plot(x2,0,'gD')
plt.plot(x3,0,'bD')
plt.text(1,70,'$f(x) = x^3 - 2x^2 - 9x + 10$')
plt.text(x1,-10,'$x_1$')
plt.text(x2,-10,'$x_2$')
plt.text(x3,-10,'$x_3$')

plt.savefig('6-3.pdf')
plt.close()

