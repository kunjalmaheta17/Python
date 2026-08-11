# Write a program to iterate over lists strings and dictionaries using loops.

#iterate over lists
fruits=["Apple","Banana","Mango"]

print("Print Fruits:")
for i in fruits:
    print(i)

#iterate over strings

name="python"

for ch in name:
    print(ch)

# Iterate over a Dictionary
print("Iterating over a Dictionary:")
student = {
    "Name": "Kunjal",
    "Age": 20,
    "Course": "MCA"
}

for key,value in student.items():
    print(key, ":", value)
