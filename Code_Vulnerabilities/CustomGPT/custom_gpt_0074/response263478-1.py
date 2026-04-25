
def foo(row, f, *additional_args):
    # Unpack indices from the function specification
    indices = f.get('indices', [])
    # Get the specific elements from row based on the indices
    args = [row[i] for i in indices]
    # Call the specified function with unpacked arguments
    return f['func'](*args, *additional_args)

# Example functions to use with foo
def func1(a, b):
    return a + b

def func2(a, b, c='default'):
    return a * b + c

# Updated fList structure
fList = [
    {'func': func1, 'indices': [1, 0]},  # Pass row[1] and row[0] to func1
    {'func': func2, 'indices': [0, 1]},  # Pass row[0] and row[1] to func2
]

# Row sample
row = [5, 3, 8]  # Example row

# Calling foo
result1 = foo(row, fList[0])                 # Will call func1(3, 5)
result2 = foo(row, fList[1], c=10)           # Will call func2(5, 3, c=10)

print(result1)  # Output: 8
print(result2)  # Output: 25
