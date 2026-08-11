#  Write a program to demonstrate list dictionary and set comprehensions.

print("List Comprehension")
numbers = [10, 20, 30, 40, 50]
square_list = [x * x for x in numbers]
print(square_list)

print()

print("Dictionary Comprehension")
square_dict = {x: x * x for x in numbers}
print(square_dict)

print()

print("Set Comprehension")
square_set = {x * x for x in numbers}
print(square_set)
