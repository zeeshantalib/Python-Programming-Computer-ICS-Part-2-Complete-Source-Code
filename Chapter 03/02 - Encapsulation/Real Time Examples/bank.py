class BankAccount:
    def __init__(self, owner, account_no, pin):
        self.owner = owner              # Public
        self._account_no = account_no   # Protected
        self.__pin = pin                # Private

    def show_info(self):
        print("Owner:", self.owner)
        print("Account Number:", self._account_no)
        print("PIN:", self.__pin)

account = BankAccount("Ali", "123456789", "1234")

print(account.owner)         # Public
print(account._account_no)   # Protected (possible but discouraged)

# print(account.__pin)       # Error

account.show_info()