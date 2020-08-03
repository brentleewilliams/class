'''
# Simple pass

class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (99, 95, 87, 88, 65)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades[2])
print(student.average_grade())

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Rolf", (99, 95, 11, 88, 12))
student2 = Student("Dolf", (99, 95, 11, 28, 12))
student3 = Student("Solf", (99, 95, 11, 88, 12))

print(student2.average_grade())
# two ways to do the same thing.
print(Student.average_grade(student2))


numbers = [2, 4, 6, 8]
product = 1
for number in numbers:
    product *= number

print(f'The product is:', product)    


def f1ib1(n):
    a = 0
    b = 1
    while a < n:
        print(a,b, end=' ')
        a, b = b, a+b
        print(a, b)
    
f1ib1(1000)



def f1ib1(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

f1ib1(1000)
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def __repr__(self):
        return f"{self.name} {self.age}"


bob = Person("Bob", 35)
#print(Person(self.name)
print(bob)