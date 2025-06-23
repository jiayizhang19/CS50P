"""
Reference link: https://docs.python.org/3/library/functions.html#open

Use csv module to reader csv file with more complicated content instead of directly using open().
    -> Note: No space should be there in csv file after each comma, otherwise it will casue "ValueError: too many values to unpack (expected 2)" 

Use csv.reader() to read each line inside csv file as a list, see csv.DictReader() in students_V2.1.py

"""

import os
import csv

file_path = os.path.join(os.path.dirname(__file__), "students_reader_V2.0.csv")

students = []
with open(file_path) as file:
    reader = csv.reader(file) 
    for name, home in reader:
        student = {"name": name, "home": home}
        students.append(student)

print(students)

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is from {student['home']}.")