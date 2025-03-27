distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from the Earth.")

    print("========== CONVERSIONS BELOW ==========")
    
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} meters.")


def convert(distance):
    return distance * 149597870700

main()