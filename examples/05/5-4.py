# File 5-4.py
# Example 5. Plots
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt
import numpy as np

# the data
t = np.array([0, 60, 120, 240, 360])
c = np.array([0, 0.1, 0.2, 0.8, 1.9])
# ploting
plt.plot(t, c, 'rD')
plt.title('5-4.pdf')
plt.xlabel('t, a.u.')
plt.ylabel('c, a.u.')
plt.savefig('5-4.pdf')
plt.close()
