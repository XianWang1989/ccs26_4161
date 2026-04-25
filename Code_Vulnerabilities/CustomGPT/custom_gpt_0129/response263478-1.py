
def foo(row, f):
    """
    Passes specified elements from row to function f in the given order
    and allows for static arguments.
    """
    # Extract the function and its arguments
    func = f[0]
    args = f[1:]

    # Prepare the arguments to pass to the function
    processed_args = []

    for arg in args:
        if isinstance(arg, int):  # If arg is an index
            processed_args.append(row[arg])
        else:  # Otherwise, it's a static value
            processed_args.append(arg)

    return func(*processed_args)

# Example functions
def func1(x, y, z):
    return x + y * z

def func2(a, b):
    return a - b

def func3(word1, word2):
    return f"{word1} and {word2}"

# Example usage
row = [10, 20, 30, 40, 50]

fList = [
    (func1, 1, 0, 4),  # func1(row[1], row[0], row[4])
    (func2, 2, 1),     # func2(row[2], row[1])
    (func3, 'Hello', 'World')  # static arguments
]

for f in fList:
    print(foo(row, f))
