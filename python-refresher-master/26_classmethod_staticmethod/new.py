'''
class ClassTest:
    def instance_method(self):
        print(f"Called insance_method of {self}")
        #used most of the time to do things
    
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
        #used as factories

    @staticmethod
    def static_method():
        print("Called static_method.")
        #Simply used when you want to store a method within a particular class

#ClassTest.class_method()
ClassTest.static_method()

# test = ClassTest()
# test.instance_method()

'''

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        #way to print out values in a class
        return f"<Book is {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        #can use cls or the specific class name of book
        return cls(name, cls.TYPES[0], page_weight + 100)
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)



book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(book)
print(light)

