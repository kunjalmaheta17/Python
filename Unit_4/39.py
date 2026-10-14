#Write a program to read and write data into a file using different file modes.

#Write to file
f = open("data.txt", "w")
f.write("Hello Python")
f.close()

#Append to file
f = open("data.txt", "a")
f.write("\nWelcome to Python")
f.close()

#Read from file
f = open("data.txt", "r")
print(f.read())
f.close()
