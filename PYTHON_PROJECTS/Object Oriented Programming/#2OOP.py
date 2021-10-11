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

    @classmethod  # This format turns regular method into class method. It is called a decorator.
    def set_raise_amount(cls, amount):  # This method sets the raise amount for the class.
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):  # This method creates new employee
        first, last, age, pay = emp_str.split('-')
        return cls(first, last, age, pay)

    @staticmethod  # Static methods do not operate on any instance of the class.
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # Monday is 0, Sunday is 6 while the rest lie in between.
            return False
        return True


Employee.set_raise_amount(1.2)  # The class method enables us to set the raise amount for all employees in the class.

emp_1 = Employee('Shanza', 'Allan', 20, 150000)  # This is an instance of class Employee.
emp_2 = Employee('Ogude','Allan', 25, 200000)  # This is another instance of class Employee


my_date = datetime.date(2020, 4, 10)
print(Employee.is_workday(my_date))

'''emp_str_1 = 'Peter-Pata-20-90000'
emp_str_2 = 'Joy-Linda-20-70000'
emp_str_3 = 'Olivia-Chelsea-21-80000'
new_emp_1 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)'''