"""
Use (?P<name>) in regular expressions to name the group, access it with .group("name") instead of .group(1)
"""

import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    number = input("Phone Number: ")
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    matches = re.search(pattern, number)
    if matches:
        country_code = matches.group("country_code")
        try:
            print(locations[country_code])
        except KeyError:
            print("Not registered in the system.")
    else:
        print("Invalid number.")


if __name__ == "__main__":
    main()