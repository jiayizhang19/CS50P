"""
In a file called numb3rs.py, implement a function called validate that 
expects an IPv4 address as input as a str and then returns True or False, 
respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main 
and/or implement other functions as you see fit, but you may not import any other libraries. 
You’re welcome, but not required, to use re and/or sys

"""

import re

def main():
    address = input("IPv4 Address: ")
    print(validate(address))


def validate(address):
    pattern = r"^(\d{1,3}\.){3}(\d{1,3})$"
    if re.search(pattern, address):
        return all(0 <= int(num) <= 255 for num in address.split("."))
    else:
        return False

if __name__ == "__main__":
    main()
