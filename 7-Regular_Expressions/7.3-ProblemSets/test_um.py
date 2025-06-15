from um import *

def test_um_in_word():
    assert count("yummy") == 0


def test_um_in_the_middle():
    assert count("hello, um, world, um, end") == 2


def test_startswith_um():
    assert count("um... hello") == 1


def test_endswith_um():
    assert count("hello, um") == 1


def test_um_case():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um") == 1



