"""
See regular expression documentation in details as followed:
https://docs.python.org/3/library/re.html

regular expression symbols:
. --> any character except a newline
* --> 0 or more repetitions
+ --> 1 or more repetitions
? --> 0 or 1 repetition
{m} --> m repetitions
{m,n} --> m-n repetitions
^ --> matches the start of the string
$ --> matches the end of the string or just before the newline at the end of the string
[] --> set of characters
[^] --> complementing the set
    For examplpe:
        .* means zero or more chanacter(s);
        .+ means one or more character(s), or using ..* refers to the same meaning 

\d --> decimal digit, 0-9
\D --> not a decimal digit
\s --> whitespace characters
\S --> not a whitespace character
\w --> word character ... as well as numbers and the underscore
\W --> not a word character
    For example, the below emial pattern could be rewritten as:
    pattern = r"^\w+@\w+\.edu$"

A|B --> either A or B
() --> a group
(?:) --> non-capturing version
    

Use a raw string by prefixing the string with "r" when using escape letter (\)
The regular expression still works without a "r", but Python will raise a warning.
As the backslash(\) is used for escape sequences in strings -- like:
    \n for newline
    \t for tab
    \\ for a literal backslash
So, \. is not a recognized escape in Python strings, hence the warning 
"""

import re

email = input("What's your email? ").strip()

# pattern = r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(edu|gmail|org|ie)$"
pattern = r"^\w+@(\w\.)?\w+\.edu$"

if re.search(pattern, email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")