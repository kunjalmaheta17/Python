#Write a program to copy move and delete files using shut il module. 

import shutil
import os

# Copy a file
shutil.copy("source.txt", "copy.txt")
print("File copied successfully.")

# Move a file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully.")

# Delete a file
os.remove("moved.txt")
print("File deleted successfully.")
