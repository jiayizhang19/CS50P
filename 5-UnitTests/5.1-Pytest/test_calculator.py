"""
Note: filenames and foldernames cannot start with digits or contain dashes if you want to import them as modules.

"""

from calculator import square

def test_square_using_if():
    if square(2) == 4:
        print("2 squared was 4.")
    if square(3) == 9:
        print("3 squared was 9.")


if __name__ == "__main__":
    test_square_using_if()
    