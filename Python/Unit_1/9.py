# Write a program to define and use user-defined functions with different types of arguments.

#define user-defined functions
def greetings():
    print("Welcome to python...")

# 1.Positional Arguments

def add(a,b):
    print("Sum:",a+b)
add(10,20)

# 2.Keyword Arguments

def student(name,surname):
    print("Your name is ",name,surname)
student(name="kunjal",surname="maheta")

# 3.Default Arguments

def details(name,subject="python"):
    print("welcome to ",subject,name,"!!")
details(name="Kunjal")

# 4.Variable-Length Arguments

def total(*numbers):
    print(numbers)

total("kunjal","maheta")
total(10, 20, 30, 40)
    



    
