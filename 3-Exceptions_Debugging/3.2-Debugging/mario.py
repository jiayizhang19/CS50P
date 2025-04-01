"""
1. add breakpoints
2. click on run and debug button to launch debugging
3. use debug toolbar to step through the code
    --> continue: continue to the next breakpoint
    --> step over: step over the current line
    --> step into: step into the function call
    --> step out: step out of the current function
"""

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

if __name__ == "__main__":
    main()