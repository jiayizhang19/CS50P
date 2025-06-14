from working import *
import pytest

def test_midday_AM():
    assert midday("0", ":00", "A") == "00:00"
    assert midday("9", ":59", "A") == "09:59"
    assert midday("12", "", "A") == "00:00"


def test_midday_PM():
    assert midday("0", ":00", "P") == "12:00"
    assert midday("9", ":59", "P") == "21:59"
    assert midday("12", "", "P") == "12:00"


def test_convert_valid():
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"


def test_convert_invalid_time_format():
    with pytest.raises(ValueError):
        convert("my working time is from 9:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("nine AM to five PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 5: PM")


def test_convert_omit():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:30 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 5:30 PM")


def test_convert_time_outof_range():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 13:00 PM")
