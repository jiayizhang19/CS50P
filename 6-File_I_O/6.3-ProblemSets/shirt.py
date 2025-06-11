"""
Use shirt.png, before1.jpg, before2.jpg, before3.jpg as reference.

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, 
saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, 
per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, 
using default values for method, bleed, and centering, overlay the shirt with Image.paste, 
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, 
and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.

"""

from PIL import Image, ImageOps
import sys


def main():
    before, after = is_valid()
    overlay(before, after)


def is_valid():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].lower().endswith(("jpg", "jpeg", "png")) and sys.argv[2].lower().endswith(("jpg", "jpeg", "png"))):
        sys.exit("Invalid input")
    elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
        sys.exit("Input and output have different extensions")
    else:
        return sys.argv[1], sys.argv[2]


def overlay(before, after):
    try:
        with Image.open(before) as img, Image.open("shirt.png") as shirt:
            img = ImageOps.fit(img, shirt.size)
            img.paste(shirt, shirt)
            img.save(after)
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
