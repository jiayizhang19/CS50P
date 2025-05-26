"""
Note: 
Assert statement we are using here, is designed to test arguments into functions and return values they're from. Not testing side effects.



"""

from hello import hello

def test_hello():
    assert hello("jiayi") == "hello, jiayi"


