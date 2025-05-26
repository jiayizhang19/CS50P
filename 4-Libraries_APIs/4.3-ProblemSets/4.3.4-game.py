"""
In a file called game.py, implement a program that:

Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
"""

import random


def main():
    level = get_positive_number("Level")
    num = random.randint(1, level)
    while True:
        guess = get_positive_number("Guess")
        if guess == num:
            print("Just right!")
            break
        elif guess > num:
            print("Too large!")
        else:
            print("Too small!")


def get_positive_number(pro):
    while True:
        try:
            user_input = int(input(f"{pro}: "))
            if user_input > 0:
                return user_input
        except ValueError:
            pass


if __name__ == "__main__":
    main()
