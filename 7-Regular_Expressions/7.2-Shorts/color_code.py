"""
.group() --> return the entire match
.group(0) --> same as above
.group(n) --> return the specific part of the match

"""

import re

def main():
    color_code = input("Color Code: ")
    pattern = r"^#[a-f0-9]{6}$"
    matches = re.search(pattern, color_code, re.IGNORECASE)
    if matches:
        print(f"Valid. Matched with {matches.group()}")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()