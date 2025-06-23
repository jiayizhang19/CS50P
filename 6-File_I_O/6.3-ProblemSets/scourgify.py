"""
Use before.csv as reference.

In a file called scourgify.py, implement a program that:
Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

Note that csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, 
among which are DictReader, per docs.python.org/3/library/csv.html#csv.DictReader 
and DictWriter, per docs.python.org/3/library/csv.html#csv.DictWriter.
Note that you can tell a DictWriter to write its fieldnames to a file using writeheader with no arguments, 
per docs.python.org/3/library/csv.html#csv.DictWriter.writeheader.
"""

import sys
import csv

def main():
    input_file, output_file = is_valid()
    write_new_file(input_file, output_file)


def is_valid():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not (sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv")):
        sys.exit("Not csv file")
    else:
        return sys.argv[1:]


def write_new_file(input_file, output_file):
    try:
        with open(input_file) as origin, open(output_file, "w") as new:
            reader = csv.DictReader(origin)
            writer = csv.DictWriter(new, fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                writer.writerow(
                    {
                        "first": row["name"].split(",")[1].strip(),
                        "last": row["name"].split(",")[0].strip(),
                        "house": row["house"]
                    }
                )
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
