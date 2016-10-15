# File 3-1.py
# Example 3. Calculations with Python
# Copyright (C) 2016, Szczepan Bednarz
# Released under the GNU General Public License

def eq1(x):
    return x**2

def eq2(x,y):
    z = x+y
    return z

def eq3(x):
    return x**p

x = 4
result = eq1(x)
print result      # 16

x=1
y=9
print eq2(x,y) # 10

p = 3
x = 2
print eq3(x) # 8
