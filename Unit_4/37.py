#Write a program to illustrate method resolution order and magic methods.

#Method Resolution Order (MRO)
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()

print(C.mro())

#Magic Method
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Rahul")
print(s)
