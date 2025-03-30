"""
"break" is used to exit the nearest enclosing for/while loop, but pay attention to "if" conditions:
 --> 1. if put "break" inside "if" conditions, it will do as many iterations inside the loop before it achieves break condition
 --> 2. if put "break" in the parallel with the "if" conditions, then it will only do once iteration inside the loop.
Take the below two "break" usage, line23 and line29 inside the for loop as reference.

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    is_valid = True
    if plate.isalnum() and 2 <= len(plate) <= 6 and plate[:2].isalpha():
        for char in plate:
            if char.isdigit():
                if char == "0":
                    is_valid = False
                break # it is in the parallel level with the if condition, so the code will only check the first digit then break the loop
        if is_valid:
            for i in range(2,len(plate)-1):
                if plate[i].isdigit():
                    if plate[i+1].isalpha():
                        is_valid = False
                        break # it is inside the if condition, so the code will check as many times as it will before reaching the break
    else:
        is_valid = False
    return is_valid


main()



