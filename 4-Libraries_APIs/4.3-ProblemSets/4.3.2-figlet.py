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
            if comm not in ('-f', '--font') or font not in all_fonts:
                sys.exit('Invalid usage.')
    except ValueError as e:
        sys.exit(e)

    user_input = input('Input: ')
    text = set_to_figlet(user_input, font)
    print('Output:', text, sep='\n')

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

if '__init__' == '__main__':
    main()