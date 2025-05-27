"""
We have to use pytest.raises() to check exceptions, instead of using assert 

"""

import pytest
from convert import convert

def test_integer():
    assert convert(1) == 149597870700


def test_float():
    assert convert(3.3) == 3.3 * 149597870700


def test_string():
    with pytest.raises(TypeError):
        convert("cat")


def test_string_format_number():
    # assert convert("1") == "TypeError: au must be an integer or float"
    with pytest.raises(TypeError):
        convert("1")