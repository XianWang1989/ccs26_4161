
def foo(row, f):
    # Check if f is a string or an integer
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract the function and its argument specifications
        func, args = f
        resolved_args = []

        for arg in args:
            # If the argument is a string, return it as is
            if isinstance(arg, str):
                resolved_args.append(arg)
            # If it's an int, get it from the row
            elif isinstance(arg, int):
                resolved_args.append(row[arg])
            # If it's a callable, invoke it with the row
            elif callable(arg):
                resolved_args.append(arg(row))

        return func(*resolved_args)

# Example functions
def func1(x, y):
    return x + y

def func2(x, static):
    return x * static

# Example usage
row_example = [10, 20, 30, 40, 50]

fList = [
    (func1, [0, 2]),          # func1 with row[0] and row[2]
    (func2, [1, 5]),          # func2 with row[1] and static 5
    'Hello, World',           # Just a string
    3                         # Access row[3]
]

for f in fList:
    result = foo(row_example, f)
    print(result)
