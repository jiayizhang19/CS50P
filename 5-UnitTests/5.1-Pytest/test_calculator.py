"""
Note: filenames and foldernames cannot start with digits or contain dashes if you want to import them as modules!!!

Unit Test options in Python:
    1. Using if statements to manually catch bugs per condition.
    2. Using assert to automatically catch bugs per condition, however, it needs to be used along with try-except for clarity.
    3. Using Pytest to automatically catch bugs in high efficiency.
Note: 
    1. Option 1 and 2 need explicitly call test functions, while option 3 does not.
    2. No need to import pytest and only run the file start with pytest in the command line. 
       Only need to import it if need to access some functions inside pytest, see def test_str()

"""


from calculator import square
import pytest


# Option 3: The most recommended way for unit test
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negetive():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")




# # Option 1: Using if statement
# def test_square_using_if():
#     if square(2) == 4:
#         print("2 squared was 4.")
#     if square(3) == 9:
#         print("3 squared was 9.")


# # Option 2: Using assert
# def test_square_using_assert():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4.")
    
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9.")


# # Only explicitly call functions for Option 1 and 2, no need to call it for option 3.
# if __name__ == "__main__":
#     # test_square_using_if()
#     test_square_using_assert()
    