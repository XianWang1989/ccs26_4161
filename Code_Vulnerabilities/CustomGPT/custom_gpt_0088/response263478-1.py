
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f[0]):
        func = f[0]
        args = []
        for arg in f[1]:
            if isinstance(arg, int):
                args.append(row[arg])
            elif isinstance(arg, str):
                args.append(arg)  # Allow static strings
            else:
                raise ValueError("Unsupported argument type")
        return func(*args)
    else:
        raise ValueError("Invalid function format")

# Example functions
def func1(a, b):
    return a + b

def func2(a, b, static):
    return a * b + static

# Example row
row = [10, 20, 'spam', 'eggs', 5]

# Function list
fList = [
    (func1, [0, 1]),                  # Uses row[0] and row[1]
    (func2, [2, 4, 'static']),        # Uses row[2], row[4], and a static string
    'Hello, World',                   # Just a static string
    1                                  # Index to access row[1]
]

# Testing the functions
for f in fList:
    print(foo(row, f))
