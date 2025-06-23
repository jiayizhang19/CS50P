"""
Suppose that you’d like to implement a cookie jar in which to store cookies. 
In a file called jar.py, implement a class called Jar with these methods:

1. __init__ should initialize a cookie jar with the given capacity, 
which represents the maximum number of cookies that can fit in the cookie jar. 
If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

2. __str__ should return a str with n * 🍪, where n is the number of cookies in the cookie jar. 
For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

3. deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, 
though, deposit should instead raise a ValueError.

4. withdraw should remove n cookies from the cookie jar. Nom nom nom. 
If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.

5. capacity should return the cookie jar’s capacity.

6. size should return the number of cookies actually in the cookie jar, initially 0.

"""

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self,n):
        if n + self.size > self.capacity:
            raise ValueError("Too many cookies to be added")
        else:
            self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Too few cookies to be removed")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0 or not isinstance(capacity, int):
            raise ValueError("Not a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n




