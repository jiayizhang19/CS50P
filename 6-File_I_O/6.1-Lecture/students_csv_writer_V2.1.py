"""
Reference link: https://docs.python.org/3/library/functions.html#open

Same as csv.DictReader(), csv.DictWriter() is used to write to the file specifically as a dictionaty.
Note: pass the column sequence in a list as the value of second arguments "fieldnames" of csv.DictWriter()
"""

import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "students_writer_V2.1.csv")

name = input("What's your name? ")
home = input("Where do you live in? ")

with open(file_path,"a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home": home})
