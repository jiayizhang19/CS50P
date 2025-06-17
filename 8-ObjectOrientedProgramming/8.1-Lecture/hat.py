import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    def sorting(self, name):
        print(name, "is in ", random.choice(self.houses))


hat = Hat()
hat.sorting("Harry")