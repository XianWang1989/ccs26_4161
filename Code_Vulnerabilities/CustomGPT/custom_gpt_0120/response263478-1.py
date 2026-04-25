
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        func, *args = f
        # Extract values from row based on the specified indices
        values = [row[i] if isinstance(i, int) else i for i in args]
        return func(*values)

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a):
    return a * 2

def func3(s1, s2):
    return f"{s1} {s2}"

# Example dataset row
row = [10, 20, 30, 'spam', 'eggs']

# Function list with flexible argument specification
fList = [
    (func1, 0, 1, 2),          # Uses elements at indices 0, 1, and 2
    (func2, 3),                # Uses element at index 3
    (func3, 'hello', 'world'), # Static arguments
    'Hello, World',
    1                          # Direct index
]

# Testing the functions
for f in fList:
    result = foo(row, f)
    print(result)  # Outputs: 60, 'spamspam', 'hello world', 'Hello, World', 20
