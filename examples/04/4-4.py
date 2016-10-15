# File 4-4.py
# Example 4. Arrays in Python

import numpy as np

# Creation of array (matrix) 2x3 (2 columns, 3rows):
m1 = np.array([[10,20],[30,40],[50,60]])
print(m1)

# Addressing one element [row_index][column_index]:
print( m1[0][0] )      # 10 - a first element - first column & row
print( m1[1][1] )      # 40 - a second column & row

# Addressing selected column (colon means all elements):
print('columns')
print( m1[:,0] )      # a first column (vector!)
print( m1[:,1] )      # a second column (vector)

# and selected rows:
print('rows')
print( m1[0,:] )      # a first row (vector)
print( m1[1,:] )      # a second row (vector)
print( m1[-1,:] )     # the last one (3rd) (also vector)


