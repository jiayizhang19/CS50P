"""
In a file called professor.py, implement a program that:

Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. 
No need to support operations other than addition (+). Prompts the user to solve each of those problems. 

If an answer is not correct (or not even a number), 
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. 

If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

"""

import random

def main():
    level = get_level()
    corr_nums = 0
    ques_nums = 0
    while ques_nums < 10:
        attempts = 0
        # x, y = random.choices(generate_integer(level), k=2)
        x, y = [generate_integer(level) for _ in range(2)]
        corr_answer = x + y
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                attempts += 1
            else:
                if answer == corr_answer:
                    corr_nums += 1
                    break
                elif answer != corr_answer:
                    print("EEE")
                    attempts += 1
        if attempts == 3:
            print(f"{x} + {y} = {corr_answer}")
        ques_nums += 1
    print(f"Score: {corr_nums}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level in [1, 2, 3]:
                return level
            else:
                continue


def generate_integer(level):
    max_num = 10 ** level
    min_num = 10 ** (level - 1)
    if level == 1:
        return random.randint(0, max_num - 1)
    else:
        return random.randint(min_num, max_num - 1)
    # return [i for i in range(min_num, max_num)]
    # return random.choices(num_list, k=2)


if __name__ == "__main__":
    main()
    # print(generate_integer(2))
    # x, y = random.choices(generate_integer(2), k=2)
    # print(x,y)
