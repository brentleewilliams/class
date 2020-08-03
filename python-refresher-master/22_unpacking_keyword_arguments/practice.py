""""

def named(**kwargs):
    print(kwargs)

named(name="Bob", age=25)


def named(name, age):
    print(name, age)

details = {"name": "bob", "age": 25}

named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name = "Bob", age = 24)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,4,6, name="Brian", age=23, name2="Brian")

"""

def myfunction(**kwargs):
    print(kwargs)


dic2 = {"name": "Brent", "age" : 25, "sex" : "Male"}

myfunction(**dic2)