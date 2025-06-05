"""
1. sorted(iterables, key=, reverse=)
    -> a function can be passed to the key argument
    -> avoid passing get_name() to the key instead get_name, as sorted() will call get_name() automatically, see Task 2, Approach 1

2. using lambda funtion in key argument if the defined function is only used once, see Task 2, Approach 2
    e.g. sorted(students, key=lambda s: s["name"],reverse=True)
    -> The lambda doesn't "know" about students directly. Instead, sorted() passes each element of students to the lambda as s.
    -> The for loop later just iterates over the sorted list—it doesn't affect the lambda
"""

import os

file_path = os.path.join(os.path.dirname(__file__), "students.csv")


""" ----------------------- Task One: print student name and house in content's order ----------------------- """
# with open(file_path) as file:
#     for line in file:
#         """
#         Instead of using 
#          -> row = line.rstrip().split(",") then pass parameters like row[0] and row[1],
#         use unpack feature in python to assign values to variables directly like below.
#         """
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}.")


""" ----------------------- Task Two: print student name and house by name in ascending order ----------------------- """
    # --------------------- Approach One: Pass regular funtion to the key statement inside sorted() ---------------------
# students = []
# with open(file_path) as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

    # --------------------- Approach Two: Pass anonymous function to the key statement inside sorted() ---------------------
students = []
with open(file_path) as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda s: s["name"],reverse=True):
    print(f"{student['name']} is in {student['house']}")