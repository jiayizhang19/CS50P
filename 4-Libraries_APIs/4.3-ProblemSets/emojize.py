'''
Prompts the user for a str in English and then outputs the “emojized” version of that str, 
converting any codes (or aliases) therein to their corresponding emoji.
See reference link here :https://pypi.org/project/emoji/
'''

import emoji

def main():
    user_input = input('Input: ')
    print('Output:', emoji.emojize(user_input, language='alias'))
    
main()