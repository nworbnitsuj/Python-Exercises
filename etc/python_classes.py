#Python Classes

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.initial = first[:1] + last[:1]
        self.email = first + '.' + last + '@DrangusMail.com'



emp_1 = Employee('Jimmy', 'Jangles')
emp_2 = Employee('Steve', 'Brule')
print('{} {}, your email is {} {}'.format(emp_1.first, emp_1.last, emp_1.email, emp_1.initial))
print('{} {}, your email is {} {}'.format(emp_2.first, emp_2.last, emp_2.email, emp_2.initial))
