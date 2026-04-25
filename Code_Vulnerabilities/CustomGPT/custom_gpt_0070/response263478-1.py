
def foo(row, f, *static_args):
    if callable(f):  # Check if f is a callable
        return f(*static_args, *[row[i] for i in f.__code__.co_varnames if i.isdigit()])
    return f  # Directly return if not callable

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

def func3(arg1, arg2):
    return f"{arg1} and {arg2}"

# Example usage
row = [10, 20, 30, 40, 50]
fList = [
    (func1, 1, 0),        # func1 with two elements from row
    (func2, 2),          # func2 with one element from row
    (func3, 0, 3, 'hello') # func3 with elements from row and a static argument
]

for func in fList:
    print(foo(row, func[0], *func[1:]))
