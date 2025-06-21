"""
Although __str__ has been defined to return a formatted string, 
it is still required to write str(jar) instead of jar in assertion.
When pytests is doing comparation, jar is still accounted for the format of object, 
thus need to turn object jar with formatted string into string. before comparing it to the assertion string.

"""

from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert jar == ""
    jar.deposit(3)
    assert jar == "🍪🍪🍪"


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(12)
    jar.deposit(10)
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


