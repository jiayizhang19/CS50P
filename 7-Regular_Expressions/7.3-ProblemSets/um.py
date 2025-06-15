"""
Recall that the re module comes with quite a few functions, 
per docs.python.org/3/library/re.html, including findall.

Note that \b is “defined as the boundary between a \w and a \W character (or vice versa), 
or between \w at the beginning/end of the string,” 
per docs.python.org/3/library/re.html#regular-expression-syntax.

You might find regex101.com or regexr.com helpful for testing regular expressions (and visualizing matches).
"""

import re

def main():
    text = input("Text: ")
    print(count(text))


def count(s):
    pattern = r"\bum\b"
    l = re.findall(pattern, s, re.IGNORECASE)
    return len(l)

if __name__ == "__main__":
    main()
