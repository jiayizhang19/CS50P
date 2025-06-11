"""
See PEP here for python formatting: https://peps.python.org/pep-0008/.
Below tools can be used to automatically your code.
    1. pip install pylint
    2. pip install pycodestyle: https://pycodestyle.pycqa.org/
    3. pip install black: https://black.readthedocs.io/ --> run black xxx.py in the terminal window to get it automatically formatted.
"""

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
    "Padma": "Ravenclaw",
}
for student in students:
    print(student)
