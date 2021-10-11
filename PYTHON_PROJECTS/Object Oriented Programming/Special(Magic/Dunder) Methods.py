# Class methods and static methods
import datetime


class Employee:  # This is a class named Employee which has two methods; the __init__ method and Fullname method.
    raise_amount = 1.15
    num_of_employees = 0

    def __init__(self, first, last, age, pay):  # This method takes five arguments. It runs every time we create new.
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_employees += 1

    def fullname(self):  # This is a method that takes instance as the first argument
        return '{} {}'.format(self.first, self.last)  # It returns the full name of the employees.

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Or Employee.pay. This is because it is a class variable.

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay, self.email)


emp_1 = Employee('Shanza', 'Allan', 20, 150000)  # This is an instance of class Employee.
emp_2 = Employee('Ogude','Allan', 25, 200000)  # This is another instance of class Employee.

print(emp_1)
