# Write a program to demonstrate conditional statements using if if-else and if-elif-else.

name = input("Enter Student Name: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n----- STUDENT RESULT -----")
print("Student Name :", name)
print("Total Marks  :", total, "/500")
print("Percentage   :", percentage, "%")

if percentage >= 90:
    print("Grade : A+")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade : B")
elif percentage >= 60:
    print("Grade : C")
elif percentage >= 35:
    print("Grade : D")
else:
    print("Grade : F (Fail)")
