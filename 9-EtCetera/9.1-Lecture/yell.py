"""
map(function, iterable, ...)
[Note]: function inputted here should not be called, instead it works as a reference (function without parantheses), 
see example:
    use map(str.upper, words) instead of map(str.upper(), words),
    use map(int, texts) instead of map(int, texts).



"""

def main():
    yell("This", "is", "CS50")
    numbers("12", "23", "45")


def yell(*words):

    """ ================== Approach One: Use for loop =================="""
    # uppercased = []
    # for word in words:
    #     uppercased.append(word.upper())

    """ ================== Approach Two: Use map() to replace the above three lines ================== """
    # uppercased = map(str.upper, words)

    """ ================== Approach Three: Use list comprehension ================== """
    uppercased = [word.upper() for word in words]
    print(*uppercased)


def numbers(*texts):
    texts = map(int, texts)
    print(*texts)


if __name__ == "__main__":
    main()