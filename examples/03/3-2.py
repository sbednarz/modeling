# File 3-2.py
# Example 3. Calculations with Python
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

def eq1(x):
    print x[0]
    print x[1]
    return x[0]+x[1]

a0 = 3
b0 = 7
result = eq1([a0,b0])
print result

c0 = [a0, b0]
result = eq1(c0)
print result
