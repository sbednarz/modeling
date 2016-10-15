# File 4-1.py
# Example 4. Arrays in Python

import numpy as np

# Lets create a small one-dimensional array - vector:
v1 = np.array( [2,4,6] )
# Please remember about module_alias-dot-function_name notation

print(v1)                       # 3 elements: 2,4,6
print( v1[0] )                  # first element (index = 0) 
print( v1[1] )                  # first element (index = 1) 
print( v1[2] )                  # first element (index = 2) 

print('sum of elements')
print( v1[0] + v1[1] + v1[2] )  # sum of the vector elements

# You can do also some arithmetic operations (element-by-element mode):
print( v1+2 )
print( v1**2 )

v2 = 3*v1
print( v2 )
