# File 4-2.py
# Example 4. Arrays in Python

import numpy as np

v1 = np.array( [2,4,6] )

# You can apply math functions from NumPy module,
# simply pass name of the array (vector) to a function:

print( np.log10(v1) ) # log10 of each v1 element

# Please note v1 vector is unchanged
print(v1)

# To save the results you can create new vector:
v2 = np.log10(v1)
print(v2)
