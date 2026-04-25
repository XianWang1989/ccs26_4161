
def foo(row, f):
    if isinstance(f, str):
        return f  # return string directly
    elif isinstance(f, int):
        return row[f]  # return indexed row element
    elif callable(f):
        # Handle function calls with user-specified arguments
        return f(**{key: row[idx] if isinstance(idx, int) else idx for key, idx in f.items()})
    else:
        raise ValueError("Unsupported function format")

# Example usage
def func1(a, b, c):
    return a + b + c

def func2(name, times):
    return f"{name}!" * times

# fList configuration
fList = [
    {"f": func1, "args": {"a": 1, "b": 0, "c": 4}},
    {"f": func2, "args": {"name": "Hello", "times": 2}},
    "Just a string",
    2
]

row = [10, 20, 30, 40, 50]

for f in fList:
    if isinstance(f, dict):
        result = foo(row, f['args'])
    else:
        result = foo(row, f)
    print(result)
