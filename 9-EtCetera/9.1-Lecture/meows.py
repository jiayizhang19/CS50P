"""
1. constant:
Python does not actually make variables constant. 
Capitalize the variables only indicates to others not to touch it, it is a constant.
But there is literally nothing in the code preventing others from changing it.

2. type hints:
use annotation syntax, such as:
    "n: int" for variable annotations,  
    " -> str" for function annotations,
as well as mypy tool for early bug detection, using
    mypy xx.py

3. docstrings:
standardize how you should document your functions among other aspects of your code. 


"""

# ===================== 1. constant =====================
# class Cat:

#     MEOWS = 3
    
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()


# ===================== 2. type hints =====================
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")


# ===================== 3. docstrings =====================
def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an integer
    :return: a string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * 3
