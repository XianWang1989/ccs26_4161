
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        func, *args = f
        # Prepare the arguments to pass to the function
        resolved_args = []
        for arg in args:
            if isinstance(arg, int) or isinstance(arg, slice):
                resolved_args.append(row[arg])
            else:
                resolved_args.append(arg)  # static value
        return func(*resolved_args)

# Example functions
def func1(x, y, static_value):
    return x + y + static_value

def func2(a):
    return a * 2

# Example fList
fList = [
    (func1, 1, 0, 5),  # func1 with row[1], row[0], and a static value 5
    (func2, 4),        # func2 with row[4]
    'Hello, World',
    2                  # directly accessing row[2]
]

# Example row
row = [10, 20, 30, 40, 50]

# Testing the foo function
for f in fList:
    result = foo(row, f)
    print(result)
