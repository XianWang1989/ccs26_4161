
def foo(row, f, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Pass the row elements and any additional keyword arguments to the function
        return f(**{**kwargs, **{k: row[i] for i, k in enumerate(kwargs.keys())}})

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x ** 2

def func3(arg1, arg2):
    return f"{arg1} and {arg2}"

# Example row
row = [10, 20, 30, 40, 50]

# Example usage
fList = [
    (func1, dict(a=1, b=0, c=4)),
    (func2, dict(x=1)),
    (func3, dict(arg1='spam', arg2='eggs')),
    'Hello, World',
    2
]

# Testing foo function
for function, args in fList:
    result = foo(row, function, **args)
    print(result)
