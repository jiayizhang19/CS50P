"""
when using () in the pattern of re.search(), it could return both the boolean value, 
as well as the specific value of the group using:
    .groups() to return all the values of the group, or
    .group() to return the value of one specific group. 


:= is used in python to:
firstly, assign value from right to left,
secondly, ask boolean question about it (e.g. if or elif question) in the same line.
    For example, the below code could be simplified to:
        if matches := re.search(r"^(.+), *(.+)$", name):
            ...
            
"""

import re

name = input("What's your name? ")
pattern = r"^(.+), *(.+)$"
matches = re.search(pattern, name)
if matches:
    # Approach One:
    # last, first = matches.groups()
    # name = f"{first} {last}"

    #Approach Two:
    name = f"{matches.group(2)} {matches.group(1)}"
    # name = matches.group(2) + " " + matches.group(1)


print(f"hello, {name}")