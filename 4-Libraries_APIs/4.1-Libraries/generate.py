'''
1. It is highly recommended to separate error handling logic from main business logic, see Option 2.
2. Use sys.exit() to exit prematurely if the program itself just cannot proceed. Note, it will exit the whole program itself without execute any further codes.
'''

import sys

# Option 1:
# try:
#     print("Hello, my name is", sys.argv[1]) # Here sys.argv[0] points to the name of the file.
# except IndexError:
#     print("Too many or too few arguments.")

# Option 2: Separate error handling logic from business logic
if len(sys.argv) > 2:
    sys.exit('Too many arguments.')
elif len(sys.argv) < 2:
    sys.exit('Too few arguments.')
print('Hello, my name is', sys.argv[1])

# Another example of sys.exit() without the use of sys.argv
# cards = ['jack','queen','king']
# if len(cards) < 5:
#     sys.exit('Cards are less than 5')
# print(cards)