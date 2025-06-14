"""
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats 
and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. 
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats 
or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). 
But do not assume that someone’s hours will start ante meridiem and end post meridiem; 
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

"""

import re

def main():
    hours = input("Hours: ")
    print(convert(hours))


def convert(time):
    pattern = r"^(\d|1[0-2])(:[0-5][0-9])? (A|P)M to (\d|1[0-2])(:[0-5][0-9])? (A|P)M$"
    matches = re.search(pattern, time)
    if matches:
        fir = midday(matches.group(1), matches.group(2), matches.group(3))
        sec = midday(matches.group(4), matches.group(5), matches.group(6))
        return f"{fir} to {sec}"
    else:
        raise ValueError


def midday(h, m, mid):
    h = int(h)
    if mid == "A":
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    m = m if m else ":00"
    return f"{h:02}{m}"

if __name__ == "__main__":
    main()
