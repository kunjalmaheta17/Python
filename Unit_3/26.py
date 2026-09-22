#Write a program to perform file and directory operations using os and sys modules.

import os
import sys

#Display current working directory
print("Current Directory:", os.getcwd())

#Create a new directory
directory = "MyFolder"
if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory created:", directory)
else:
    print("Directory already exists:", directory)

#List files and directories
print("Contents of current directory:")
print(os.listdir())

#Display Python version using sys module
print("Python Version:", sys.version)

#Display command-line arguments
print("Command-line Arguments:", sys.argv)

#Change directory
os.chdir(directory)
print("Changed Directory:", os.getcwd())

#Return to parent directory
os.chdir("..")
print("Back to Directory:", os.getcwd())
