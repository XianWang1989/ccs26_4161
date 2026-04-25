
def foo(row, func, **kwargs):
    # Combine row values and additional kwargs
    arguments = {**kwargs}

    # If the key exists within row, update arguments with the row values
    for key in arguments.keys():
        if isinstance(arguments[key], int) and arguments[key] < len(row):
            arguments[key] = row[arguments[key]]

    return func(**arguments)

# Example functions to use with foo
def func1(a, b):
    return a + b

def func2(x, multiplier=1):
    return x * multiplier

# Example usage
row = [10, 20, 30, 40]
fList = [
    (func1, {'a': 0, 'b': 1}),  # Passing row[0] and row[1]
    (func2, {'x': 2, 'multiplier': 3})  # Passing row[2] with additional static argument
]

# Call foo with each function and its arguments
for func, args in fList:
    result = foo(row, func, **args)
    print(result)
