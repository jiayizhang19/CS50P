"""
.pop() function is used to REMOVE a specific key-value pair from the dictionary.
It requires the KEY as argument, and returns the VALUE associated with that key!!!
Differences between dictionary and list regarding .pop():
    1. In dictionary, it requries a KEY and returns the associated VALUE.
    2. In list, it requires an INDEX and returns the element. 

.clear() function is used to remove ALL key-value pairs from the dictionary.

.items() function is used to iterate over all the keys and values in the dictionary.
"""

words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    text = input("Do you want to play the game or get the answer? "
                 "\n(1 for the game and 2 for the answer): ")
    if text == "1":
        guess_the_word()
    elif text == "2":
        return_the_full_dic()
    else:
        print("Please provide 1 or 2.")


def guess_the_word():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    while len(words) > 0:
        print(f"{len(words)} words left!")
        guess = input("Guess a word: ")
        if guess == "GRAPHIC":
            words.clear()
            print("You've won!")
        elif guess in words.keys():
            points = words.pop(guess)
            # print(f"You've got {words[guess]} points!")
            print(f"You've got {points} points!")
        
    print("That's the game!")

def return_the_full_dic():
    print("Welcome to the Spelling Bee!")
    for word, points in words.items():
        print(f"{word} is worth {points} points!")

main()

