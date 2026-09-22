#Write a program to generate random numbers using random module.

import random

#Generate random numbers
print("Random integer:", random.randint(1, 100))
print("Random float:", random.random())
print("Random number between 10 and 50:", random.uniform(10, 50))

#Generate multiple random numbers
print("Five random integers:")
for i in range(5):
    print(random.randint(1, 100))
