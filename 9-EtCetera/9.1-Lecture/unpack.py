"""
Using the * to unpack a list / tuple into positional arguments. It can be used with any iterable types.
    *coins == coins[0], coins[1], coins[2]
Using the ** to unpack a dictionary into keyword arguments.
    **coins == coins['galleons'], coins['sickles'], coins['knuts']

Using the *args to accept a variable number of positional arguments in a function.
Using the **kwargs to accept a variable number of keyword arguments in a function.
"""

# ============= Function to unpack list and disctionary =============
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
print(total(*coins), "Knuts")

coins_dict = {'galleons': 100, 'sickles': 50, 'knuts': 25}
print(total(**coins_dict), "Knuts")

# ============= Function with *args and **kwargs =============
def f(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

f(1, 2, 3, a=4, b=5)