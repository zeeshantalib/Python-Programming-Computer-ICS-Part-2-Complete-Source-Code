class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name                 # Public
        self._employee_id = employee_id  # Protected
        self.__salary = salary           # Private

    def show_record(self):
        print("Employee:", self.name)
        print("Employee ID:", self._employee_id)
        print("Salary:", self.__salary)

emp = Employee("Usman", "EMP001", 60000)

print(emp.name)
print(emp._employee_id)
# print(emp.__salary)

emp.show_record()