"""
Note: 
Assert statement we are using here, is designed to test arguments into functions and return values they're from. Not testing side effects.

For example, if hello function is written as below, there will be failures to test it, as it only has side effect, instead of a return value.
def hello(to="world"):
    print("hello,", to)

"""

from hello import hello

def test_hello():
    assert hello("jiayi") == "hello, jiayi"


