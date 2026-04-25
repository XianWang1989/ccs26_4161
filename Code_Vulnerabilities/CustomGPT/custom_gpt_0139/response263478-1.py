
def foo(row, f):
    # If f is a string or int, simply return it
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract function and its parameters
        func, *params = f
        # Collect the arguments to pass to the function
        args = []
        for param in params:
            if isinstance(param, int):   # If it’s an index, get from row
                args.append(row[param])
            elif callable(param):         # If it’s a callable object, append its result
                args.append(param())
            else:                         # Otherwise just append the value
                args.append(param)
        return func(*args)

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

# Usage with fList
fList = [
    (func1, 1, 0),   # func1 with elements at index 1 and 0 from row
    (func2, 3),      # func2 with element at index 3 from row
    ('Hello, World'),# Just a string
    (len, 'Some static string'), # Length of a static string
    2                 # An integer from the row
]

# Example row data
row_data = [10, 20, 30, 40]

# Testing the foo function
for f in fList:
    result = foo(row_data, f)
    print(result)
