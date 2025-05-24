"""
In a file called adieu.py, implement a program that prompts the user for names, one per line,
until the user inputs control-d. (Note: control-d applies only on github copilot, while in here should be control-z-enter) 
Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and,
and names with commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa

Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect.
"""

import inflect


def main():
    names = get_user_input()

    # Approach 1:
    # if len(names) <= 2:
    #     names = ' and '.join(names)
    # else:
    #     first_part = ', '.join(names[:-1])
    #     names =  first_part + ', and ' + names[-1]

    # Approach 2: Use libraries inflect
    p = inflect.engine()
    names = p.join(names)

    print(f"Adieu, adieu, to {names}")


def get_user_input():
    user_inputs = []
    while True:
        try:
            user_input = input("Name: ")
        except EOFError:
            print("\n", sep="")
            break
        else:
            user_inputs.append(user_input)

    return user_inputs


if __name__ == "__main__":
    main()
