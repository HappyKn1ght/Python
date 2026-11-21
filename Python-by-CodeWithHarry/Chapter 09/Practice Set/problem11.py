# 11. Write a python program to rename a file to “renamed_by_python.txt”.

# with open("this.txt", "r") as f:
#     content = f.read()

# with open("renamed_by_python.txt", "w") as f:
#     f.write(content)

import os

os.rename("this.txt", "renamed_by_python.txt")
print("renamed successfully")