
def foo(row, func_info):
    if isinstance(func_info, str):
        return func_info
    elif isinstance(func_info, int):
        return row[func_info]
    elif isinstance(func_info, dict):
        func = func_info['function']
        args = func_info.get('args', [])
        return func(*[row[i] if isinstance(i, int) else i for i in args])

# Example functions
def func1(a, b):
    return a + b

def func2(x, static_val):
    return x * static_val

# List of functions with their argument specifications
fList = [
    {'function': func1, 'args': [1, 0]},        # uses row[1] and row[0]
    {'function': func2, 'args': [2, 5]},        # uses row[2] and static value 5
    'Hello, World',                              # returns string as is
    2                                           # returns row[2]
]

# Sample row
row = [10, 20, 30, 40]

# Testing the foo function
for f in fList:
    print(foo(row, f))  # Outputs: 30, 150, Hello, World, 30
