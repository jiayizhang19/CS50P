"""
enumerate(iterable, start=0) is used to iterate over some sequence to find both the value one at a time and the index thereof.
"""

students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i+1, students[i])

for i, student in enumerate(students,start=1):
    print(i, student)

