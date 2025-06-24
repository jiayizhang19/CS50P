"""
argparse:
Using argparse to handle command line with options and arguments.
    --> python meows_argparse.py -h to check the help message.
[Note]: The attribute name is based on the long option name, or the inferred from the last name if no long 
option name specified. It means, using args.n instead if --number is not specified.
"""
#Approach Two: Using argparse
import argparse

parser = argparse.ArgumentParser(description="Print 'meow' like a cat.")
parser.add_argument("-n", "--number", type=int, default=1, help="number of times to meow")
args = parser.parse_args()

for _ in range(args.number):
    print("meow")

# Apporach One: Using sys.argv
# import sys
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("Usage: python meows_argparse.py [-n <number>]")
#     print("If -n is specified, it should be followed by a number indicating how many times to print 'meow'.")
