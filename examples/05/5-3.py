# File 5-3.py
# Example 5. Plots
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,60)
y1 = 3*x+10
y2 = 0.1*x**2 - 3*x + 10

plt.plot(x,y1,'b-', label='y1')
plt.plot(x,y2,'g-', label='y2')
plt.title('5-3.pdf')
plt.xlabel('x, a.u.')
plt.ylabel('y1, y2, a.u.')
plt.legend(loc='upper left')      # loc = location
plt.savefig('5-3.pdf')
plt.close()
