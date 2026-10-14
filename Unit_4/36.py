#Write a program to demonstrate method overriding and polymorphism.

#Method Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")


#Polymorphism
a = Dog()
b = Cat()

a.sound()
b.sound()
