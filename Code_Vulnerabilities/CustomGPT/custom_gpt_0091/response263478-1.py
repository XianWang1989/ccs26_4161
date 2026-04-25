
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f()  # Call the function without arguments
    else:
        func, *args = f
        resolved_args = [row[i] if isinstance(i, int) else i for i in args]
        return func(*resolved_args)

# Example functions
def func1(x, y):
    return x + y

def func2(x, y, z):
    return x * y + z

def func3(static_arg):
    return f"Static Argument: {static_arg}"

# Example dataset
row = [3, 5, 2, 7]

# Example function list
fList = [
    (func1, 0, 1),                 # func1 with row[0] and row[1]
    (func2, 0, 2, 10),             # func2 with row[0], row[2], and static 10
    (func3, 'Static Value'),       # func3 with a static string
    'Hello, World',                # Just a string
    1                               # row[1]
]

# Running the test
for f in fList:
    print(foo(row, f))
