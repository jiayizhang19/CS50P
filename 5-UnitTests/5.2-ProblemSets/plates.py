# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
def main():
    plate = input()
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
                break
        if is_valid:
            for i in range(2,len(plate)-1):
                if plate[i].isdigit():
                    if plate[i+1].isalpha():
                        is_valid = False
                        break
    else:
        is_valid = False
    return is_valid

if __name__ == "__main__":
    main()
