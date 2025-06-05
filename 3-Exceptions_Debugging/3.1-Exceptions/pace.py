"""
raise statement is used to trigger exceptions.
    --> use Exception("...") directly
    --> raise built-in exceptions like ValueError("..."), TypeError("...") and KeyError("...")
    --> define your own exceptions by inheriting from the Exception class
        class CustomError(Exception):
            pass
        def check_value():
            if x < 0:
                raise CustomError("Value can not be negative.")

"""

def main():
    miles, minutes = input("Please input your miles and minutes: ").split()
    pace = get_pace(float(miles), float(minutes))
    print(f"Your pace need to be {round(pace, 2)} miles per minute.")

def get_pace(miles, minutes):
    if minutes <= 0:
        raise ValueError("Minutes should be greater than 0.")
    else:
        return miles / minutes
    
main()