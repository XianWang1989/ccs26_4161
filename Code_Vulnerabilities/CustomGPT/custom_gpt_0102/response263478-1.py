
def foo(row, f, *args):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract the specified indices from row
        return f(*[row[i] for i in f['indices']] + list(args))

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(a, b):
    return a * b

# Redefining fList with structured outputs
fList = [
    {'func': func1, 'indices': [1, 0, 4]},  # Indices map to 'row'
    {'func': func2, 'indices': [3]},        # Another example
    'Hello, World',
    2
]

# Sample data_row
data_row = [10, 20, 30, 40, 50]  # Example row

# Using foo
result1 = foo(data_row, fList[0]['func'], indices=fList[0]['indices'])
result2 = foo(data_row, fList[1]['func'], 2)  # Passes static args too

print(result1)  # Output should be the result of func1
print(result2)  # Output should be the result of func2
