#Write a program to demonstrate different import mechanisms in Python.

import module_1
print("- Using import module:")
print("Addition:", module_1.add(10, 5))

from module_1 import add
print("\n- import function:")
print("Addition:", add(20, 10))

from module_1 import add, multiply
print("\n- import multiple functions:")
print("Addition:", add(30, 10))
print("Multiplication:", multiply(30, 10))

import module_1 as m
print("\n- as alias:")
print("Addition:", m.add(40, 10))
print("Multiplication:", m.multiply(40, 10))
