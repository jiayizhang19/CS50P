"""
Given a dictionary representing a spacecraft, create a report that includes the spacecraft's name and distance from Earth. 
If the distance is not provided, use "Unknown" as the default value.
Use update() to add multiple key-value pairs to the dictionary.
"""

def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft["orbit"] = "Heliosphere"
    spacecraft.update({"distance": 0.01, "size": "Small"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    =========== REPORT ===========
    Name: {spacecraft["name"]}
    Distince: {spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("orbit", "Unknown")}
    Size: {spacecraft.get("size", "Unknown")}
    ==============================
    """

if __name__ == "__main__":
    main()