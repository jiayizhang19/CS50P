"""
global:
A global variable could be read directly while can not be written in the same way without using the keyword global.
Even moving balance into main() does not work, as the balance here is still a local variable to main(), instead of deposit() and withdraw().

"""
# Approach One
# balance = 0

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)


# def deposit(n):
#     global balance
#     balance += n


# def withdraw(n):
#     global balance
#     balance -= n


# if __name__ == "__main__":
#     main()


# Approach Two: Using class
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()