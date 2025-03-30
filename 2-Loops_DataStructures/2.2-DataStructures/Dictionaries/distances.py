"""
.keys() is used to extract all keys in the dictionary.
 --> It is the same not using .keys() to check keys in the dictionary, and such approach is much more efficient.
 --> While using .keys() makes code much more readable but less efficient as it first retrieves a view then checks for membership.

.values() is used to extract all values in the dictionary.
.items() is used to extract keys and values in the dictionary. --> see examples in the bee.py
"""

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    # it is the same using "for name in distances:" instead of "distances.keys()"
    for name in distances.keys(): 
        print(f"{name} is {distances[name]} AU from the Earth.")

    print("========== CONVERSIONS BELOW ==========")
    
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} meters.")


def convert(distance):
    return distance * 149597870700

main()