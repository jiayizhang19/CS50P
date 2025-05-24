"""
FIGlet has since been ported to Python as a module called pyfiglet: https://pypi.org/project/pyfiglet/

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

"""

from pyfiglet import Figlet
import sys
import random


def main():
    try:
        if len(sys.argv) == 1:
            font = select_font()
        else:
            comm, font = sys.argv[1:]
            all_fonts = get_all_fonts()
            if comm not in ("-f", "--font") or font not in all_fonts:
                sys.exit("Invalid usage.")
    except ValueError as e:
        sys.exit(e)

    user_input = input("Input: ")
    text = set_to_figlet(user_input, font)
    print("Output:", text, sep="\n")


def set_to_figlet(text, font):
    figlet = Figlet()
    figlet.setFont(font=font)
    text = figlet.renderText(text)
    return text


def select_font():
    all_fonts = get_all_fonts()
    font = random.choice(all_fonts)
    return font


def get_all_fonts():
    figlet = Figlet()
    all_fonts = figlet.getFonts()
    return all_fonts


if __name__ == "__main__":
    main()
