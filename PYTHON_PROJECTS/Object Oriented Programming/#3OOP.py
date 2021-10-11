# Class inheritance-creating subclasses.


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


class Engineers(Employee):  # This class will have all the attributes if the class Employee.
    raise_amount = 1.154

    def __init__(self,first, last, age, pay, department):
        super().__init__(first, last, age, pay)
        self.department = department


class Manager(Employee):  # This class shows the employees that the manager is in charge of.
    def __init__(self,first, last, age, pay, employees=None):  # This method allows us to add employees under manager.
        super().__init__(first, last, age, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):  # This method adds employees to the list of employees.
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):  # This method removes employees from the list.
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('->', emp.fullname())


emp_1 = Engineers('Lee', 'George', 20, 150000, 'Mechanical')  # This is an instance of class Engineers.
emp_2 = Engineers('Victor', 'Aminiel', 25, 200000, 'Programming')
emp_3 = Engineers('Shanza', 'Allan', 20, 150000, 'Electronics')
emp_4 = Engineers('Ogude','Allan', 25, 200000, 'Design and Architecture')

manager = Manager('Joel', 'Mumo', 21, 160000, [emp_1, emp_2, emp_4])

manager.add_employee(emp_3)

print(manager.email)
manager.print_employees()  # Prints out all the employees supervised by the manager.

#print(help(Engineers))