"""
------------------------- An instructor for operator overloading -------------------------

Similiar could be done for -,*,/ like + in the below, 
per https://docs.python.org/3/reference/datamodel.html#special-methods-names

Although there is only an argument named other beside self in the __add__(self, other),
it can indeed add more than two vaults, as when doing 
    potter + weasley + granger,
Python evaluate it as 
    (potter + weasley) + granger;
which means, this will call:
    1. potter + weasley --> returns a Vault
    2. That result + granger --> calls __add__ again
"""

class Vault:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

granger = Vault(10, 10, 10)
print(granger)

total = potter + weasley + granger
print(total)

