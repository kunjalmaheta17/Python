# Write a program to extract specific information from a text file using regular expressions.

import re

with open("data.txt", "r") as file:
    text = file.read()

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

phone_numbers = re.findall(r'\b\d{10}\b', text)

dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

print("Email Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phone_numbers:
    print(phone)

print("\nDates:")
for date in dates:
    print(date)
