
def foo(row, f, *args):
    if callable(f):
        return f(*args, **{k: row[i] for k, i in args})
    return f

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x ** 2

# Example usage
row = [10, 20, 30, 40]
fList = [
    (func1, [('a', 1), ('b', 0), ('c', 3)]),  # passing specific indexes
    (func2, [('x', 2)])                        # 'x' is not from row, static value
]

for f, args in fList:
    result = foo(row, f, *[arg for name, idx in args])
    print(result)
