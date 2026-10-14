#Write a program to perform file pointer operations using seek and tell methods. 

#File pointer operations

f = open("data.txt", "w+")
f.write("Hello Python")

print("Position:", f.tell())

f.seek(0)

print("Position after seek:", f.tell())
print("Data:", f.read())

f.close()
