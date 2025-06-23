"""
This is a upgraded design for student.py using the combination of instance variabels and methods, with class methods

"""

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        # Call the class constructor (__init__) with arguments name and house, return a new instance
        # It is equivalent to return Student(name, house)
        return cls(name, house)


def main():
    print(Student.get())


if __name__ == "__main__":
    main()