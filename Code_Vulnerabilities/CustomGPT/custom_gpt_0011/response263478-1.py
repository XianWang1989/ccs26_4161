
def foo(row, f, *static_args, **kwargs):
    # Prepare the arguments to be passed to the function
    args = [row[i] for i in kwargs.get('indices', [])] + list(static_args)
    return f(*args)

# Example functions
def func1(x, y):
    return x + y

def func2(a, b, message):
    return f"{message}: {a * b}"

# Example usage
row = [10, 20, 30, 40, 50]
fList = [
    (func1, {}, 1, 2),  # Pass row elements at indices 1 and 2
    (func2, {'indices': [0, 1]}, "Result"),  # Pass row elements at indices 0 and 1 with a static string
]

for f, kwargs, *static_args in fList:
    result = foo(row, f, *static_args, **kwargs)
    print(result)
