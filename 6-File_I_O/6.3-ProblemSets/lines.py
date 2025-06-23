"""
in a file called lines.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a Python file, and outputs the number of lines of code in that file, 
excluding comments and blank lines. If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.

"""

import sys

def main():
    file = is_valid()
    print(calculate_lines(file))


def is_valid():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
    else:
        return sys.argv[1]


def calculate_lines(file):
    number = 0
    try:
        with open(file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    number += 1
    except FileNotFoundError:
        sys.exit("File does not exit")
    return number


if __name__ == "__main__":
    main()
