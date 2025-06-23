"""
Use regular.csv as reference.
In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, 
a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.

Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
Note that the tabulate package comes with just one function, per pypi.org/project/tabulate. You can install the package with:
pip install tabulate

"""

from tabulate import tabulate
import sys
import csv

def main():
    file = is_valid()
    print(format_table(file))


def is_valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        return sys.argv[1]


def format_table(file):
    try:
        with open(file) as f:
        # Approach 1: use csv.reader()
            # reader = csv.reader(f)
            # return tabulate(reader, headers="firstrow", tablefmt="grid")
        # Approach 2: use csv.DictReader()
            reader = csv.DictReader(f)
            return tabulate(reader, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
