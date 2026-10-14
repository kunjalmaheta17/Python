#Write a program to illustrate instance variables and class variables.

class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 20)
student2 = Student("Priya", 21)

print("Student 1 Name:", student1.name)
print("Student 1 Age:", student1.age)

print("Student 2 Name:", student2.name)
print("Student 2 Age:", student2.age)

print("School:", Student.school)

Student.school = "XYZ School"

print("Updated School:", student1.school)
print("Updated School:", student2.school)
