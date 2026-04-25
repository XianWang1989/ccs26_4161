
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        func, args = f
        resolved_args = []
        for arg in args:
            if isinstance(arg, int):
                resolved_args.append(row[arg])
            else:
                resolved_args.append(arg)
        return func(*resolved_args)

# Example functions
def func1(a, b):
    return a + b

def func2(a):
    return a * 2

# Example usage
row = [3, 5, 7, 9]  # Sample row
fList = [
    (func1, [1, 0]),  # func1 will receive row[1] and row[0]
    (func2, [2]),     # func2 will receive row[2]
    ('Hello, World',),  # static string
    (lambda x: x * 3, [0]),  # inline function with row[0]
]

for f in fList:
    result = foo(row, f)
    print(result)
