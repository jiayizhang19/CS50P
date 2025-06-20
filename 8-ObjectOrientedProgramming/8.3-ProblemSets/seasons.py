"""
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
and then sings prints how old they are in minutes, rounded to the nearest integer, 
using English words instead of numerals, just like the song from Rent, without any and between words. 
Since a user might not know the time at which they were born, assume, for simplicity, 
that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. 
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. 
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Note: Note that the date class comes with quite a few methods and “supported operations,” 
per docs.python.org/3/library/datetime.html#date-objects. In particular, the class implements __sub__, 
per docs.python.org/3/library/operator.html#operator.__sub__, overloading - in such a way that subtracting 
one date object from another returns a timedelta object, 
which itself comes with several (read-only) “instance attributes,” 
per docs.python.org/3/library/datetime.html#timedelta-objects.
"""

from datetime import date
import sys
import inflect

def main():
    date_of_birth = input("Date of Birth: ")
    mins = calculate_mins(date_of_birth)
    print(f"{convert_to_words(mins)} minutes")
    # print(mins)

def calculate_mins(birth_date):
    today = date.today()
    try:
        year, month, day = birth_date.split("-")
        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")
    d = today - birth_date
    return d.days * 24 * 60


def convert_to_words(num):
    p = inflect.engine()
    words = p.number_to_words(num)
    return words.replace(" and ", " ").capitalize()


if __name__ == "__main__":
    main()


