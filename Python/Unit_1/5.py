# Write a program to create and manipulate lists using indexing slicing and list comprehensions. 

college = ["MCA","MBA","MCOM","M.ED","M.PHARM"]

#indexing
print("First Field : "+college[0])
print("First Field : "+college[-1])

#slicing
print("Slice fields: ",college[2:])
print("Slice fields: ",college[2:4])
print("Slice fields: ",college[:4])

#List Comprehension
numbers = [1,2,3,4,5]
square = [x*x for x in numbers]

print("Numbers:", numbers)
print("Squares:", square)


