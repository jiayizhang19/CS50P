from PIL import Image
from PIL import ImageFilter
import os

in_path = os.path.join(os.path.dirname(__file__),"in.jpg")
out_path = os.path.join(os.path.dirname(__file__),"out.jpg")

def main():
    with Image.open(in_path) as image:
        img = image.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save(out_path)

if __name__ =="__main__":
    main()