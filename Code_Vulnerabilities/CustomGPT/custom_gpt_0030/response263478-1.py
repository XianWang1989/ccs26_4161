
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int)):
        return row[f]
    elif callable(f):
        return f()
    elif isinstance(f, tuple):
        func = f[0]
        args = []
        for arg in f[1:]:
            if isinstance(arg, int):
                args.append(row[arg])
            else:
                args.append(arg)
        return func(*args)
    else:
        raise ValueError("Unsupported type in function list")

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

# Function list
fList = [
    (func1, 0, 1),                  # Calls func1 with row[0], row[1]
    (func2, 4),                     # Calls func2 with row[4]
    (lambda: "Hello, World"),      # Static string function
    (func1, 2, 3, "static value")  # Calls func1 with row[2], row[3] and a static value
]

# Example dataset
row = [10, 20, 30, 40, 50]

# Using the function handler
for f in fList:
    print(foo(row, f))
