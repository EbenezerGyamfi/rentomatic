from dataclasses import dataclass
from datetime import date


# class Employee:
#     yearly_raise = 0.5

#     def __init__(self, salary):
#         self.salary = salary

#     def get_salary(self):
#         return self.salary
#     @classmethod
#     def increase_raise(cls, salary):
#        cls.yearly_raise += salary
#        return cls.yearly_raise
#     @staticmethod
#     def print_date():
#         return date.today()


# emp = Employee(4000)


# print(emp.get_salary())
# print(emp.increase_raise(4000))



# class Student(Employee):
#     def __init__(self, salary, grade):
#         super().__init__(salary)
#         self.grade = grade
#     @property
#     def email(self):
#         return f'ebenezer.gyamfi@regent.edu.gh'

#     @email.setter
#     def email(self, email):

#          print(email)


#     def get_grade(self):
#         return self.grade

#     def __repr__(self):
#         return f'Student(grade={self.grade}, salary={self.salary})'


# studen = Student(0.0,6.9)
# studen.email = 'ebenezer.rentmann@regent.edu.gh'
# print(studen.email)
# print(studen.get_salary())
# print(studen.get_grade())


# print(1 + 2)
# print('1' + '2')

# print(repr(studen))


"""
what dataclasses gives out of the box
unecessary boiler plate like __init__ and __repr__
1.Comes with free equality checker


"""

@dataclass
class language:
    name: str
    level: int


lang1 = language('Python', 95)
lang2 = language('Python', 95)


print(lang1 == lang2)

