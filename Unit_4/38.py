#Write a program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod

#Encapsulation
class Student:
    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print("Marks:", self.__marks)


#Abstraction
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

#Encapsulation
s = Student()
s.show_marks()

#Abstraction
d = Dog()
d.sound()
