'''
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100,97,88,67))
student2 = Student("dad", (100,100,88,67))
student3 = Student("red", (100,97,88,22))

print(student.name)
print(student.average_grade())
 

print(student2.average_grade())




student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))

# But wouldn't it be nice if we could...
# print(student.average()) ?



# -- Parameters in __init__ --


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (36, 67, 90, 100, 100))
print(student.average())

# -- Remember *args ? --
'''

class Student:
    def __init__(self, name, *grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", 36, 67, 90, 100, 100)
print(student.average())
