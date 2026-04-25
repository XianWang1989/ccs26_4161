
def foo(row, f, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract arguments based on the function's signature
        arg_values = []
        for arg in f.__code__.co_varnames[:f.__code__.co_argcount]:
            if arg in kwargs:
                arg_values.append(kwargs[arg])
            else:
                arg_values.append(row[arg])
        return f(*arg_values)

# Example functions
def func1(a, b, c):
    return a + b * c

def func2(x):
    return x ** 2

def func3(arg1, arg2):
    return f"{arg1} and {arg2}"

# Example row
row = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Updated fList format
fList = [
    (func1, {'b': 'b', 'a': 'a', 'c': 'c'}),  # Passing elements with keyword mapping
    (func2, {'x': 'a'}),                       # Passing square of 'a'
    (func3, {'arg1': 'spam', 'arg2': 'eggs'}) # Static arguments
]

for f in fList:
    result = foo(row, f[0], **f[1])  # Pass function and keyword arguments
    print(result)  # Prints results of each function call
