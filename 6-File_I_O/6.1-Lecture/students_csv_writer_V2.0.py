"""
Reference link: https://docs.python.org/3/library/functions.html#open

Same as csv.reader(), csv.writer() is used to write to the file specifically as a list.

"""

import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "students_writer_V2.0.csv")

name = input("What's your name? ")
home = input("Where do you live in? ")

with open(file_path,"a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
