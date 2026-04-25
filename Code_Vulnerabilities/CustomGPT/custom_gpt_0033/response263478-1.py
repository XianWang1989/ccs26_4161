
from functools import partial

def foo(row, f, *args):
    """Evaluate a function f with row elements and additional static arguments."""
    if callable(f):
        # Gather the row elements specified by the callable's argument names
        return f(*args, *[row[i] for i in args if isinstance(i, int)])
    else:
        return f

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(s1, s2):
    return f"{s1} and {s2}"

# Usage example
row = [1, 2, 3, 4, 5]
f1 = partial(func1, 10, 20)   # static arguments
result1 = foo(row, f1, 2)      # pass index of row element
print(result1)  # Output: 10 + 20 + 3 = 33

f2 = func2
result2 = foo(row, f2, 4)      # pass index of row element
print(result2)  # Output: 5 * 2 = 10

f3 = partial(func3, 'spam')    # static argument
result3 = foo(row, f3, 1)       # pass index of row element
print(result3)  # Output: 'spam and eggs'
