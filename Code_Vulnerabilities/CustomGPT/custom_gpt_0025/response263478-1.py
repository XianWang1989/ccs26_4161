
def foo(row, f, *static_args):
    if callable(f):
        # Extract arguments from the row based on their indices
        row_args = [row[i] for i in f['indices']]
        # Call the function with row arguments and static arguments
        return f['func'](*row_args, *static_args)
    elif isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]

# Example functions
def func1(a, b, static=''):
    return a + b + static

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} & {b}"

# Function list with indices and static defaults
fList = [
    {'func': func1, 'indices': [0, 1]},
    {'func': func2, 'indices': [2]},
    {'func': func3, 'indices': [3, 4]},
    'Hello, World',
    2
]

# Example row
row = [10, 20, 5, 'spam', 'eggs']

# Usage examples
print(foo(row, fList[0], static='!'))  # Calls func1 with row[0], row[1] + static
print(foo(row, fList[1]))                # Calls func2 with row[2]
print(foo(row, fList[2]))                # Calls func3 with row[3], row[4]
print(foo(row, fList[3]))                # Returns 'Hello, World'
print(foo(row, fList[4]))                # Returns row[2] which is 5
