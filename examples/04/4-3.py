# File 4-3.py
# Example 4. Arrays in Python

import numpy as np

v1 =  np.linspace(0, 10, 5) 
# start = 0
# end = 10
# number of equally spaced values (N) = 5
print(v1)

v2 =  np.linspace(-1, 1, 5) 
# start = 0 end = 10 N = 5
print(v2)                        # -1 -0.5 0 0.5 1

v3 = np.linspace(-1,1)           # default N=50
print(v3)                        # 50 equally spaced values are generated 

v4 = np.arange(0, 10, 5)         # 0 5
# start = 0 step = 5 end 10 (not included)
print(v4)

v5 = np.arange(0, 1, 0.25)       # 0 0.25 0.5 0.75
# start = 0 step = 0.25 end 1 (not included)
print(v5)
