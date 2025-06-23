"""
------------------ class variables and class methods are introduced in this file. ------------------
class variables and methods operate on the entire class itself or, in turn, all objects of that class


The main difference between class method and instance method is that, 
there is no need to instantiate an object before using any method inside it.

class serves as a different way of modeling the world, to organize some of those methods which are related to
each other a little differently.

"""

import random


class Hat:

    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    @classmethod
    def sorting(cls, name):
        print(name, "is in ", random.choice(cls.houses))



Hat.sorting("Harry")