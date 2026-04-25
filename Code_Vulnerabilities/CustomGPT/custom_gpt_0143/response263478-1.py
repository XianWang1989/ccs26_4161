
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        func, indices, *static_args = f
        args = [row[i] for i in indices] + static_args
        return func(*args)

# Example functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b + c

# Example row
row = [10, 5, 3, 2]

# Function list with indices and static arguments
fList = [
    (func1, [0, 1]),              # func1 with row[0] and row[1]
    (func2, [1, 2], 4),           # func2 with row[1], row[2], and static 4
    'Hello, World',               # string return
    2,                            # returns row[2]
]

# Testing the foo function
for f in fList:
    print(foo(row, f))
