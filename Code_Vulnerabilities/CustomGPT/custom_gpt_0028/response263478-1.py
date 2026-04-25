
def foo(row, f, *args):
    if callable(f):
        return f(*args, **{key: row[idx] for key, idx in args})  # Unpack kwargs from row
    elif isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        raise ValueError("Unsupported function type.")

# Example usage
def func1(a, b, c=0):
    return a + b + c

def func2(x):
    return x * 2

# User-defined input
f1 = (func1, ('a', 1, 2))  # (function, (key, idx, static))
f2 = (func2, ('b',))  # (function, (key,))

fList = [
    f1,  # function with row elements and static args
    f2,  # function with only row element
    'Hello, World',
    2,   # access row[2]
]

# Sample row
row = {'a': 1, 'b': 3, 2: 5}

# Processing functions from fList
for f in fList:
    if isinstance(f, tuple):
        result = foo(row, f[0], *f[1])  # Call foo with function and args
    else:
        result = foo(row, f)  # Call foo with non-function values
    print(result)
