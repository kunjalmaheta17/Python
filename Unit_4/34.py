#Write a program to demonstrate instance methods class methods and static methods.

class Student:
    school = "ABC School"

    def show(self):        
        print("Hello Student")

    @classmethod
    def school_name(cls):    
        print(cls.school)

    @staticmethod
    def add(a, b):         
        print(a + b)


s = Student()

s.show()                  
Student.school_name()     
Student.add(10, 20)       
