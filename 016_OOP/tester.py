class Employee:

    raise_ammount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Name was deleted!')

    def pay_raise(self):
        self.pay *= Employee.raise_ammount

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname) - 1

emp1 = Employee('Jack', 'Smith', 3000)
emp2 = Employee('Jane', 'Smith', 2000)

print(emp1.fullname)
emp1.fullname = 'Bob Gold'
print(emp1.first, emp2.last)
print(emp1.__dict__)

del emp1.fullname