# Object Oriented Programming
# Class variables are variable that are shared among all instances os a class.
# Instance variables are unique for each instance.


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


emp_1 = Employee('Shanza', 'Allan', 20, 150000)  # This is an instance of class Employee.
emp_2 = Employee('Ogude','Allan', 25, 200000)  # This is another instance of class Employee.


'''#print(emp_1.fullname())
#print(emp_1.email)
#print(emp_1.age)
print(emp_1.pay)
emp_1.apply_raise()'''

print(emp_1.raise_amount)
print(emp_1.pay)
'''print(emp_1.__dict__)
print(Employee.__dict__)'''
print(Employee.num_of_employees)

'''print(Employee.fullname(emp_2))
#print(emp_2.fullname())
#print(emp_2.email)
#print(emp_2.age)
#print(emp_2.pay)'''