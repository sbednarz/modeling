# File 5-1.py
# Example 5. Plots
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

import matplotlib.pyplot as plt   # matplotlib pyplot submodule
import numpy as np                # numpy

plt.plot(1,1,'ro')                # draw a red bullet at (1,1)
plt.savefig('5-1.pdf')              # save the plot to file '5-1.pdf'
plt.close()                       # finish plotting
