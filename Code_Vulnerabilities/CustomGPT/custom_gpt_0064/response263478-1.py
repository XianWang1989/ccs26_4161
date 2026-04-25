
def foo(row, *args, **kwargs):
    return args[0](*[row[i] if isinstance(i, int) else i for i in args[1]] + list(kwargs.values()))

def func1(a, b, c):
    return a + b + c

def func2(x, y=5):
    return x * y

# Example row
row = [10, 20, 30, 40, 50]

# Define function calls with indexes and static arguments
fList = [
    (func1, [0, 1, 2]),  # Choosing elements at index 0, 1, 2 from row
    (func2, [0], {'y': 4}),  # Choosing element at index 0 and static arg y=4
]

# Test the functions
for f in fList:
    print(foo(row, f))
