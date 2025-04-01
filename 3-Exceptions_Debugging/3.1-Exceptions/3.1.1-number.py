"""
try - except - else:
    try to do something 
        --> if somthing goes wrong, then go to except; 
        --> if nothing goes wrong, then go ahead with else.

except: 
    --> try to figure out what kind of error could happen instead of catching everything
    --> if nothing need to be executed, use pass

break will only exit the nearest enclosing loop, while the return will exit the whole function.
"""

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError: 
            print("It is not an integer.")
        else:
            return x
        
    # another way to simplify the code
    # while True:
    #     try:
    #         return int(input(prompt))
    #     except ValueError:
    #         print("It is not an integer")


main()