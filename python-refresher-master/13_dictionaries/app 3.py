
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:  
        return "no valid operator provided to apply ()"


print(apply(1,3,6,7, operator = "*"))

#print(multiply(1,3,5,2,6))
'''

def add(x, y):
    return x + y
    
args = 12, 2
print(add(*args))
'''