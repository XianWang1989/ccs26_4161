
def foo(row, f):
    # If f is a string, return it directly
    if isinstance(f, str):
        return f
    # If f is an integer, return the corresponding element from 'row'
    elif isinstance(f, int):
        return row[f]
    # If f is a callable (function), we will handle it
    elif callable(f):
        return f(**{k: foo(row, v) for k, v in f.__annotations__.items()})
    else:
        raise ValueError("Unsupported type for f")

# Example functions with type hints for the parameters
def func1(arg1: int, arg2: int) -> int:
    return arg1 + arg2

def func2(arg1: str, arg2: int) -> str:
    return f"{arg1} {arg2}"

# Create a mapping to easily call with named parameters
def func_wrap(func, *args):
    return func(*args)

# Let's build example row and function calls
row = [10, 20, 30, 'Hello']

fList = [
    (func_wrap, [func1, (0, 1)]),         # func1 with row[0] and row[1]
    (func_wrap, [func2, (3, 2)])          # func2 with row[3] and row[2]
]

# Evaluating fList
for f in fList:
    fn, args = f
    result = foo(row, fn(*args))
    print(result)
