"""
-------------------- instance variables and instance methods are introduced in this file. --------------------
instance variables and methods belong to or operate on specific objects -- a specific student.

a class contains:
   --> attribute, 
   --> method and 
   --> property, decorated by @ syntax, called decorators, which are functions that modify the behavior of other functions  

Attribute & Method: (see details in Version Two)
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

    def __str__(self):   --> it allows others see your object as a string via, say print(student)
        ....

Property: (see details in Version Three)
    A property is just a function that has even more defense mechanisms put into place, 
    a little more functionality implemented to prevent programmers from messing things up.
    
    Actually, unlike languages like Java which has private, public etc., in the world of Python,
    it's just the honor system, which means, if an instance variable starts with an underscore or 
    double underscore, just don't touch it.
    
    The underscore is meant to signify a convention that this is meant to be private, but it really
    just means, please don't touch this. But technically, there's nothing stopping anyone from circumventing 
    all of these mechanisms or these properties.
"""


''' ----------------------- Version One: The simpliest way of defining class -----------------------'''
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


'''----- Version Two: not good enough as it allows update attributes without validating them -----'''
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Name missing")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
    
#     def __str__(self):
#         return f"{self.name} is from {self.house}"

# def main():
#     student = get_student()
#     # --> Note Here: the below code re-sets the value and passes the validation of house attribute 
#     # --> inside __init__ even through typed one of four allowed value during instantiation
#     student.house = "Number Four, Privet Drive"
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# if __name__ == "__main__":
#     main()

''' -------------- Version Three: validate values setted outside of the instantiation --------------'''
class Student:
    def __init__(self, name, house):
        # with the use of =, python automatically calls the setter funtion house for attribute assignment
        # however, if using self._house here, the assignment directly works without error checking for future instantiation
        self.name = name
        self.house = house

    def __str__(self):
        # it is the same of using self._house here, as without using the = to do assigment, 
        # python automatically calls the getter funtion house to get the value of _house
        return f"{self.name} is from {self.house}" 
    
    @property
    def house(self):
        # The reason of using _house here is to separate the name of property and the attribute
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name


def main():
    student = get_student()
    # --> Note here: Thanks for the property, the below assignment won't work with expected ValueError triggered
    # student.house = "Number Four, Privet Drive"
    # --> however, the below code works as student.house will call setter function for error checking,
    # --> while self._house is indeed the name of attribute, so it does work
    # student._house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()