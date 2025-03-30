"""
.get() is used to return a customed value if the key is not defined in the dictionary.
.update() is used to add multiple key-value pairs to the dictionary in one go.
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