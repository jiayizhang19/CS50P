"""
Reference link: https://docs.python.org/3/library/functions.html#open

1. Using "w" inside open() will automatically open and rewrite file each time, which means, all the content will be rewrote. Use "a" alternatively.
   "r" is the default value so it is okay not providing it when reading a file.

2. Using the keyword "with" helps us avoid manually calling file.close() each time upon completion as it automatically closes the file itself. 

3. When opening a file using open(), Python returns a file object that represents the file's contents.
   This object is designed to be iterable, meaning you can loop over it line by line. So we can use for loop directly.
   Each iteration of the for loop gives you one line from the file (as a string).
   
"""

import os

file_path = os.path.join(os.path.dirname(__file__), "names.txt")

# ----------------------- Part 1: Write to the file ----------------------- 
# name = input("What's your name? ")
# with open(file_path, "a") as file:
#     file.write(f"{name}\n")

# ----------------------- Part 2: Read from the file ----------------------- 
# Option 1 - most recommended approach: using a list to hold contents
names = []
with open(file_path) as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names,reverse=True):
    print(f"Hello, {name}")

# Option 2.1
# with open(file_path) as file:
#     lines = file.readlines()
# for line in lines:
#     print("Hello, ", line.rstrip())

# Option 2.2
# with open(file_path) as file:
#     for line in file.readlines():
#         print(f"Hello, {line.rstrip()}")
