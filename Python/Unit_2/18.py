#  Write a program to illustrate variable scope using local global and nonlocal variables.

x = 10       # Global

def outer():
    y = 20   # Local 

    def inner():
        nonlocal y
        y = 30       # Changes the variable of outer()
        print("Nonlocal variable y =", y)
        print("Global variable x =", x)

    inner()
    print("Local variable y =", y)
outer()
print("Global variable x =", x)
