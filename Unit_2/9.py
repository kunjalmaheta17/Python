#  Write a program to demonstrate iterators and iterables in Python.

# Iterable
numbers = [10,20,30]

print("Iterable object:",numbers)

# iterator
it = iter(numbers)

print("\nElements using iterator:")
print(next(it))
print(next(it))
print(next(it))
