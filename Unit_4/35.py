#Write a program to implement single multilevel and multiple inheritance.

#Single Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

obj = B()
obj.showA()
obj.showB()

#Multilevel Inheritance
class C:
    def showC(self):
        print("Class C")

class D(C):
    def showD(self):
        print("Class D")

class E(D):
    def showE(self):
        print("Class E")

obj = E()
obj.showC()
obj.showD()
obj.showE()

#Multiple Inheritance
class X:
    def showX(self):
        print("Class X")

class Y:
    def showY(self):
        print("Class Y")

class Z(X, Y):
    def showZ(self):
        print("Class Z")

obj = Z()
obj.showX()
obj.showY()
obj.showZ()
