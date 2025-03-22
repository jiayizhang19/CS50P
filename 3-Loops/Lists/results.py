"""
.remove() is used to remove the first instance from the list.
.insert() is used to insert the element to the specific position.
.reverse()
.append() is used to append the specific element at the end of the list.
.extend() is used to extend elements one by one within the provided list.

"""

results = ["Mario", "Luigi", "Yoshi","Bowser","Toad"]

results.remove("Bowser")
results.insert(0,"Bowser")
results.reverse()

results.append("Koop Troopa")
results.extend(["Donkey Kong Jr.", "Princess"])

print(results)