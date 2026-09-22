#Operators

#..Arithmetic operators

a = 10
b = 3
print("--------Arithmetic operators----------")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)
print(" ")

#..Assignment Operators

print("--------Assignment Operators----------")

a = 10
a += 5
print("After += :", a)

a -= 2
print("After -= :", a)

a *= 3
print("After *= :", a)

a /= 2
print("After /= :", a)

b = 17
b %= 5
print("After %= :",b)

b = 17
b //= 5
print("After //= :",b)

b = 17
b **= 3
print("After **= :",b)
print(" ")

#..Comparison (Relational) Operators


a = 10
b = 20
print("--------Comparison (Relational) Operators----------")

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
print(" ")

#..Logical Operators

a = 10
b = 20
print("--------Logical Operators----------")

print((a < b) and (a > 5))
print((a > b) or (a > 5))
print(not (a < b))
print(" ")

#..Bitwise Operators

a = 5
b = 3

print("--------Bitwise Operators----------")

print("AND =", a & b)
print("OR =", a | b)
print("XOR =", a ^ b)
print("NOT =", ~a)
print("Left Shift =", a << 1)
print("Right Shift =", a >> 1)
print(" ")


#..Membership Operators

list1 = [10, 20, 30, 40]
print("--------Membership Operators----------")

print(20 in list1)
print(50 in list1)
print(50 not in list1)
print(" ")


#..Identity Operators

print("--------Identity Operators----------")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       
print(a is c)       
print(a is not c)   

