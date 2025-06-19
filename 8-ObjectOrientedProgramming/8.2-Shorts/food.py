class Food:
    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(self.ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    # define a function to return the instance of the class without specifying ingredients but hearts
    @classmethod
    def from_nothing(cls, hearts):
        food = Food([]) # or it could be written as food = cls([])
        # after instantiating, overwrite the hearts with provided ones
        food.hearts = cls.base_hearts + hearts
        return food


def main():
    mushroom_skewer = Food(["Mushroom", "Hearty Mushroom"])
    print(f"{mushroom_skewer.ingredients} heals {mushroom_skewer.hearts} hearts ")

    non_ingredients_skewer = Food.from_nothing(2)
    print(f"{non_ingredients_skewer.ingredients} heals {non_ingredients_skewer.hearts} hearts")


if __name__ == "__main__":
    main()