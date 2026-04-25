
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:  # Assume it's a tuple with a function and arguments
        func, args = f
        resolved_args = []

        for arg in args:
            if isinstance(arg, int):
                resolved_args.append(row[arg])
            else:
                resolved_args.append(arg)  # Static argument
        return func(*resolved_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(s1, s2):
    return f"{s1} and {s2}"

# Example usage
fList = [
    (func1, [1, 0, 4]),  # Using indices from `row`
    (func2, [2]),        # Just one index
    (func3, ['spam', 'eggs']),  # Static arguments
    'Hello, World',
    2                    # Integer index for `row`
]

row = [5, 10, 15, 20, 25]  # Sample row of data

for f in fList:
    print(foo(row, f))
