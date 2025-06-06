"""
1. csv.DictReader() also has fieldnames parameter, it could be passed directly to fieldnames of csv.DictWriter()
2. Use .writeheader() to write the title row
"""


import csv
import numpy as np
import os
from PIL import Image


input_path = os.path.join(os.path.dirname(__file__),"views.csv")
output_path = os.path.join(os.path.dirname(__file__),"analysis.csv")
base_path = os.path.dirname(__file__)

def main():
    with open(input_path) as views, open(output_path,"w", newline="") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis,fieldnames=reader.fieldnames+["brightness"])
        writer.writeheader()
        for row in reader:
            row["brightness"] = calculate_brightness(os.path.join(base_path,f"{row['id']}.png"))
            writer.writerow(row)


def calculate_brightness(file):
    with Image.open(file) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return round(brightness,2)


if __name__ == "__main__":
    main()