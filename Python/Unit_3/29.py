#Write a program to use re module functions such as match search and find all.

import re

text = "Python is easy to learn. Python is powerful and popular."

result = re.match("Python", text)
if result:
    print("match():", result.group())
else:
    print("match(): No match found")


result = re.search("powerful", text)
if result:
    print("search():", result.group())
else:
    print("search(): No match found")

result = re.findall("Python", text)
print("findall():", result)
