# File 5-2.py
# Example 5. Plots
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,60)
y1 = 3*x+10
y2 = 0.1*x**2 - 3*x + 10

plt.plot(x,y1,'b.')
plt.plot(x,y2,'g.')
plt.savefig('5-2.pdf')
plt.close()
