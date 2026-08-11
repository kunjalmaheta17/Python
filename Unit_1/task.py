name = input("Enter Student Name: ")

m1 = float(input("Enter Marks of Subject 1: "))
m2 = float(input("Enter Marks of Subject 2: "))
m3 = float(input("Enter Marks of Subject 3: "))
m4 = float(input("Enter Marks of Subject 4: "))
m5 = float(input("Enter Marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n----- Student Result -----")
print("Student Name :", name)
print("Total Marks :", total)
print("Percentage :", percentage)

# if statement
if percentage >= 35:
    print("Student is Eligible to Pass")

# if-else statement
if percentage >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")

# if-elif-else statement
if percentage >= 80:
    print("Grade : Distinction")
elif percentage >= 70:
    print("Grade : First Class")
elif percentage >= 60:
    print("Grade : Second Class")
elif percentage >= 35:
    print("Grade : Pass Class")
else:
    print("Grade : Fail")
