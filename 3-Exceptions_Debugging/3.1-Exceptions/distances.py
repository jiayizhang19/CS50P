"""
Always include return in the except bolck if the function should terminate early upon an exception.
Otherwise it will continue further execution defined in the function outside of try-except block. 

It always is a good practice to be as specific with exceptions, instead of using except to catch all errors.
"""

distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        distance = convert(float(distances[spacecraft]))
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary.")
        return
    except ValueError:
        print(f"Cannot convert '{distances[spacecraft]}' to a float.")
        return
    else:
        print(f"{distance} m away.")

def convert(distance):
    return distance * 149597870700

main()