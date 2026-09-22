#Write a program to demonstrate basic regular expression pattern matching. 


import re

# Sample text
text = "My phone number is 9876543210."

# Search for a 10-digit phone number
pattern = r"\d{10}"

match = re.search(pattern, text)

if match:
    print("Pattern matched!")
    print("Phone number:", match.group())
else:
    print("Pattern not matched.")
