class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


# Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)

print(account.get_balance())  # Output: 1200

# Direct access will fail (raises AttributeError)
# print(account.__balance)