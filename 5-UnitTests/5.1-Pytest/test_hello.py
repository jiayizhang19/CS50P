"""
Note: 
Assert statement we are using here, is designed to test arguments into functions and return values they're from. 
Not testing side effects. For example, 
if hello function is written as below, there will be failures when test it, as it only has side effect, instead of a return value.
def hello(to="world"):
    print("hello,", to)

Each of your tests should ideally be pretty simple and pretty small. 
As you don't want to write so much complicated code that your test mights might be flawed.
"""

from hello import hello

def test_default():
    assert hello() == "hello, world"


def test_arguments():
    assert hello("jiayi") == "hello, jiayi"


