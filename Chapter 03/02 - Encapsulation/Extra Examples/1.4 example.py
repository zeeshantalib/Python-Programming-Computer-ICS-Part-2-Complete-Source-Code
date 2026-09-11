#Public Member
# Public Member
class Employee:
    def __init__(self):
        self.salary = 50000      # Public Variable

employee = Employee()
print(employee.salary) 


# Private Member
class BankAccount:
    def __init__(self):
        self.__balance = 10000      # Private Variable

account = BankAccount()

print(account.__balance)

#Accessing a Private Variable Correctly
class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount()

account.show_balance()


# Protected Member

class Employee:
    def __init__(self):
        self._salary = 50000

class Manager(Employee):
    def show_salary(self):
        print("Salary:", self._salary)

manager = Manager()

manager.show_salary()