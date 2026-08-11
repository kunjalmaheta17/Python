# Write a program to generate a multiplication table using a for loop.

num = input("Enter a number: ")

if "." in num:
    num = float(num)
else:
    num = int(num)

for i in range(1, 11):
    print(num, "*", i, "=", num * i)
