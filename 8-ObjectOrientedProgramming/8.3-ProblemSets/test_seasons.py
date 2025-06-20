from seasons import *
import pytest

def test_calculate_mins_valid():
    assert calculate_mins("2024-06-20") == 365 * 24 * 60


def test_calculate_mins_invalid_date():
    with pytest.raises(SystemExit):
        calculate_mins("June 20, 2024")
    with pytest.raises(SystemExit):
        calculate_mins("2024-06")


def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
