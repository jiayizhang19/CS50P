"""
1. list comprehensions with conditional
2. filter(function, iterable) 
    --> the function here must return true or false, indicates that whether or not to include the current value from the final list.
    --> similiar to map(), function here only serves as the reference to the method, instead of really calling it with paratheses.
3. dictionary comprehensions
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# ================== Approach One: Use list comprehensions with conditions ==================
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


# ================== Approach Two: Use filter() ==================
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"
# gryffindors = filter(is_gryffindor, students)


# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])


# ================== Approach Three: Combine lamda into filter() ==================
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])


""" ************* ================== Dictionary Comprehensions ================== ************* """
students = ["Hermione", "Harry", "Ron"]

# ================== Approach One: Use for loop ==================
# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
# print(gryffindors)

# ================== Approach Two: Use dictionaty comprehensions ==================
gryffindors_list = [{"name": student, "house": "Gryffindor"} for student in students]
gryffindors_dict = {student: "Gryffindor" for student in students}
print(gryffindors_dict)
