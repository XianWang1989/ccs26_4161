
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):  # Directly pass function
        return f(*row)
    elif isinstance(f, tuple):
        func, *args = f
        # Resolve row elements if index is provided
        resolved_args = [row[i] if isinstance(i, int) else i for i in args]
        return func(*resolved_args)
    else:
        raise ValueError("Unsupported type provided to foo.")

# Example functions
def func1(a, b):
    return a + b

def func2(a):
    return a * 2

# Example usage
row = [1, 2, 3, 4, 5]
fList = [
    (func1, 0, 1),      # func1 with row[0] and row[1]
    (func2, 2),        # func2 with row[2]
    ('Hello, World',),  # Just a string
    3                   # row[3]
]

for f in fList:
    print(foo(row, f))
