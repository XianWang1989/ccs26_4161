
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Recent methods called
print(add(5, 3))        # Example of calling 'add'
print(subtract(10, 4))  # Example of calling 'subtract'
