"""
No matter for tuple, list or dictionary, we use a[xxx] to get the specifc value of it.
However in class, after instantiate student = Student(), we use student.xxx to assign or get the specific value, e.g.: 
student.name = input("Name: "), per Version One

def __init__(self, name): --> is called instance method, it runs automatically during instantiation.
    self.name = name      --> functiones similiarly to how we assign value into a dictionary, 
                              the only differance is that a dic uses [] while class uses .

Why does the instance method inside class needs variable assignment while not in regular functions?
-- As the varibales inside one class  allows other methods in the class to access it. 
   It saves the value in the object, called an instance attribute.
   However in regular function, the value is only used during the function call, it doesn't store anything long-term.

Beside the differences in approach of accessing the value between class(using .) and dictionary(using []),
the benefits of using class is that we can control what kind of values could be stored in this object.
while it is not possible in the dictionary, per Version Two.     
"""

# ----------------------- Version One: The simpliest way of defining class -----------------------
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} is from {student.house}")


# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()


# ----------------------- Version Two -----------------------
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name missing")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()