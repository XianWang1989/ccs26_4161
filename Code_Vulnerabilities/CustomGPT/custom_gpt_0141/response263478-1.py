
def foo(row, f):
    if isinstance(f, str):
        return f  # Return the string directly.
    elif isinstance(f, int):
        return row[f]  # Index into the row if given an integer.
    elif callable(f):
        return f()  # Call the function if it's callable.
    elif isinstance(f, tuple):
        func, args = f

        # Prepare the arguments
        prepared_args = []
        for arg in args:
            if isinstance(arg, int):
                prepared_args.append(row[arg])  # Use index from row
            elif isinstance(arg, str):
                prepared_args.append(arg)  # Keep string static
            elif callable(arg):
                prepared_args.append(arg())  # Call the callable
            else:
                prepared_args.append(arg)  # Handle other cases as needed

        return func(*prepared_args)  # Call the function with prepared arguments
    else:
        raise ValueError("Unsupported function format.")

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x ** 2

# Example usage
row = [10, 20, 30, 40]
fList = [
    (func1, (0, 1)),             # Passes row[0] (10) and row[1] (20) to func1
    (func2, (0,)),               # Passes row[0] (10) to func2
    ("Hello, World",),           # Just a string to return
    (func1, (1, " static")),     # Passes row[1] (20) and a static string
    (func2, (2,)),               # Passes row[2] (30) to func2
]

# Testing
for func in fList:
    result = foo(row, func)
    print(result)
