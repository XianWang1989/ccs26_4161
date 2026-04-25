
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        func, *args = f
        resolved_args = [row[x] if isinstance(x, int) else x for x in args]
        return func(*resolved_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Example usage
row = [10, 20, 30, 40, 50]
fList = [
    (func1, 2, 0, 1),  # func1 with row[2], row[0], row[1]
    (func2, 1, 5),     # func2 with row[1] and static 5
    'Hello, World',
    2                  # row[2]
]

for f in fList:
    result = foo(row, f)
    print(result)
