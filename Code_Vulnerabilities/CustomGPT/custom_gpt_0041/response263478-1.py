
def foo(row, f, *static_args, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract arguments from row based on indices in kwargs
        args = [row[idx] for idx in kwargs.get('indices', [])]
        return f(*args, *static_args)

# Example functions
def func1(a, b, c, static_val):
    return a + b + c + static_val

def func2(x):
    return x * 2

# Example usage
row = [3, 5, 1, 7, 9]
f_list = [
    (func1, {'indices': [0, 1, 2]}, 10),  # Uses row[0], row[1], row[2] + static 10
    (func2, {'indices': [3]}),            # Uses row[3] 
    "Hello, World",
    2
]

for f in f_list:
    result = foo(row, *f)
    print(result)
