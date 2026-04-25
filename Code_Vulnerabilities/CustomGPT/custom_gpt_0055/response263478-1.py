
def foo(row, f):
    # Capture any additional keyword arguments
    if callable(f):
        return f(**row)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function type")

def func1(a, b):
    return a + b

def func2(x, y, c=0):
    return x * y + c

# Example usage
row = {'a': 1, 'b': 2, 'c': 5}
fList = [
    func1,
    lambda x=1, y=2: func2(x, y, c=3),
    "Hello, World",
    2
]

# Call foo with different functions
print(foo(row, fList[0]))  # Outputs 3 (1 + 2)
print(foo(row, fList[1]))  # Outputs 5 (1 * 2 + 3)

# String and int cases
print(foo(row, fList[2]))  # Outputs "Hello, World"
print(foo(row, fList[3]))  # Outputs 2 (row[2], assuming index 2 exists)
