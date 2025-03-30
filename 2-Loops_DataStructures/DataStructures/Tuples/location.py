"""
Approaches to split a tuple coordinate:
 --> 1. coordinate[index]
 --> 2. a, b = coordinate

Differences between below two data structures:
 --> Tuple: Values within it cannot be added or changed, but it takes smaller bytes in memory.
 --> List: Values within it can be added and changed, but it takes larger bytes in memory.
"""

import sys

def main():

    coordinate = (42.375, -71.115)

    # First approach to split tuple
    # latitude = coordinate[0]
    # longitude = coordinate[1]

    # Second approach to split
    latitude, longitude = coordinate

    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    coordinate_tuple = coordinate
    coordinate_list = [42.375, -71.115]
    print(f"Tuple takes {sys.getsizeof(coordinate_tuple)} bytes.")
    print(f"List takes {sys.getsizeof(coordinate_list)} bytes.")



main()