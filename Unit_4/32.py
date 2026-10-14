#Write a program to demonstrate constructor and destructor usage. 

class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")
        print("Student name:", self.name)

    def __del__(self):
        print("Destructor called")
        print("Object destroyed")


s1 = Student("Rahul")

del s1
