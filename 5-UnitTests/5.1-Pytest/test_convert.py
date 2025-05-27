"""
Note: We have to use pytest.raises() to check exceptions, instead of assert 

"""

import pytest
from convert import convert

def test_integer():
    assert convert(1) == 149597870700


def test_float_without_toletance():
    assert convert(3.3) == 3.3 * 149597870700


def test_float_with_tolerance():
    assert convert(0.001) == pytest.approx(149597870.691)
    assert convert(0.001) == pytest.approx(149597870.691, abs=1e-5)
    

def test_string():
    with pytest.raises(TypeError):
        convert("cat")


def test_string_format_number():
    # assert convert("1") == "TypeError: au must be an integer or float" --> Incorrect way to check exception!
    with pytest.raises(TypeError):
        convert("1")