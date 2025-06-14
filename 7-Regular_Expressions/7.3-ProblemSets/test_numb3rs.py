from numb3rs import validate

def test_valid_one_digit():
    assert validate("0.0.0.0") == True
    assert validate("9.9.9.9") == True


def test_valid_two_digits():
    assert validate("10.10.10.10") == True
    assert validate("99.99.99.99") == True


def test_valid_three_digits():
    assert validate("100.100.100.100") == True
    assert validate("255.255.255.255") == True


def test_number_range():
    assert validate("0.0.0.256") == False
    assert validate("256.0.0.0") == False


def test_length():
    assert validate("0.0.0.0.0") == False
    assert validate("255.255.255") == False


def test_non_digits():
    assert validate("a.a.a.a") == False
    assert validate("....") == False


def test_starter_ending():
    assert validate("my address is 0.0.0.0") == False
    assert validate("255.255.255.255 is my address") == False
