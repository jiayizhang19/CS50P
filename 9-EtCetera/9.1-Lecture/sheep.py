"""
A generator is a lazy iterator defined by keyword yield. Each time Python hits yield, it pauses the function, 
remembers where it left off and returns one value at a time.
yield: pauses and returns a value, resumes on next call
return: exit the function immediately

"""

def main():
    n = int(input("What's the number? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐏" * i


if __name__ == "__main__":
    main()