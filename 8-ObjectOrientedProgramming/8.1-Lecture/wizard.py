"""
inherirance -- the key feature of object-oriented programming languages

super() refers to the super or parent of the currect class
.__init__(name) refers to the instance variables would like to be inheritanted here

"""

class Wizard:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    def __str__(self):
        return f"{self.name}, professor of {self.subject}"
    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

print(wizard)
print(student)
print(professor)
