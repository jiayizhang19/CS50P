"""
set() is a python data type to reduce duplicates
set().add() is equivalent to list().append()
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},    
]

# Approach using set()
houses = set()
for student in students:
    houses.add(student["house"])

# Approach without set()
# houses = list()
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

for house in sorted(houses):
    print(house)

