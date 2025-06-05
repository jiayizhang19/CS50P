"""
Reference link: https://docs.python.org/3/library/functions.html#open

Use csv.DictReader() to read each line inside csv file as a dictionary for the purpose of flexibility and fragility.
The code will always work properly no matter in which sequence the contents are inside the csv or any more contents are added, as long as the title in the first line is correct and unchanged.
Otherwise, correct or updated titles in the below code to ensure it functions well.
Note: The csv file has to have key names as the first row so that csv.DictReader() knows key-value pairs
"""

import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "students_reader_V2.1.csv")

students = []
with open(file_path) as file:
    reader = csv.DictReader(file)
    for row in reader:
        # student = {"name": row["name"], "home": row["home"]}
        # students.append(student)
        students.append(row)

print(students)

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is from {student['home']}.")

