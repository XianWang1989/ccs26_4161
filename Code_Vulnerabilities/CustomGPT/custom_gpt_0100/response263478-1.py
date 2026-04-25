
def foo(row, f):
    if isinstance(f, str):
        return f  # Return the string as is
    elif isinstance(f, int):
        return row[f]  # Return the row element at the specified index
    else:
        func, args = f[0], f[1:]
        # Unpack arguments: static values or row elements based on their type
        unpacked_args = []
        for arg in args:
            if isinstance(arg, int):
                unpacked_args.append(row[arg])  # Get value from row
            else:
                unpacked_args.append(arg)  # Static argument
        return func(*unpacked_args)  # Call the function with the unpacked arguments

# Example functions
def func1(x, y):
    return x + y

def func2(x):
    return x ** 2

def func3(a, b):
    return f"{a} and {b}"

# Example function list
fList = [
    (func1, 1, 0),       # func1 with row[1] and row[0]
    (func2, 4),         # func2 with row[4]
    (func3, 'spam', 'eggs'),  # func3 with static arguments
    'Hello, World',
    2                   # returns row[2]
]

# Example row
row = [10, 20, 30, 40, 50]

# Running the function with the various elements of fList
results = [foo(row, f) for f in fList]
print(results)  # Output: [30, 2500, 'spam and eggs', 'Hello, World', 30]
