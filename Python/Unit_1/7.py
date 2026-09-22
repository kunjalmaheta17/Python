# Write a program to create a dictionary and demonstrate dictionary methods anditeration.

student = {
    "Name": "Kunjal","Age": 20,"Course": "Python"
}

print("Original Dictionary:")
print(student)

print()

print("Keys:")
print(student.keys())

print()

print("Values:")
print(student.values())

print()

print("Items:")
print(student.items())

print()

student.update({"City": "Rajkot"})
print("After Update:")
print(student)

print()

print("Iterating through Dictionary:")
for key, value in student.items():
    print(key, ":", value)
