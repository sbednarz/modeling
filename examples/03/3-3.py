# File 3-3.py
# Example 3. Calculations with Python
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

def eq1(x):
    a = x[0]
    b = x[1]
    r1 = a+b
    r2 = a-b
    return [r1, r2]

a0 = 3
b0 = 7
result = eq1([a0,b0])
print result
print result[0]
print result[1]
