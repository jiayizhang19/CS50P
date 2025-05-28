from plates import is_valid

def test_valid_plates():
    assert is_valid("CS") == True
    assert is_valid("cs50") == True
    assert is_valid("CSprog") == True


def test_none_alnum():
    assert is_valid("cs-50") == False


def test_invalid_length():
    assert is_valid("s") == False
    assert is_valid("csprogr") == False


def test_invalid_start():
    assert is_valid("1cs") == False
    assert is_valid("c1s") == False
    assert is_valid("1234") == False


def test_leading_zero():
    assert is_valid("CS01") == False


def test_digit_in_middle():
    assert is_valid("cs50p") == False
