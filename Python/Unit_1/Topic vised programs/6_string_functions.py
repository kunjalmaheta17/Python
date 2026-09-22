# String Functions

text = "Hello Python"
text2 = "hello python"

print("Original String :", text)

# 1. upper()
print("Uppercase        :", text.upper())

# 2. lower()
print("Lowercase        :", text.lower())

# 3. capitalize()
print("Capitalize       :", text.capitalize())

# 4. title()
print("Title            :", text.title())

# 5. strip()
name = "  Kunjal  "
print("Strip             :", name.strip())

# 6. replace()
print("Replace           :", text.replace("Python", "World"))

# 7. find()
print("Position of 'Python' :", text.find("Python"))

# 8. count()
print("Count of 'o'     :", text.count("o"))

# 9. split()
print("Split             :", text.split())

# 10. join()
words = ["Python", "is", "easy"]
print("Join              :", " ".join(words))

# 11. startswith()
print("Starts with Hello :", text.startswith("Hello"))

# 12. endswith()
print("Ends with Python  :", text.endswith("Python"))

# 9. index()
print("Index of 'Python'   :", text.index("Python"))

# 13. isalpha()
print("Is Alpha          :", text.isalpha())

# 14. isdigit()
print("Is Digit          :", text.isdigit())

# 15. isalnum()
print("Is Alphanumeric   :", text.isalnum())

# 16. isspace()
print("Is Space          :", text.isspace())

# 17. islower()
print("Is Lower          :", text.islower())

# 18. isupper()
print("Is Upper          :", text.isupper())

# 19. len()
print("Length           :", len(text))


