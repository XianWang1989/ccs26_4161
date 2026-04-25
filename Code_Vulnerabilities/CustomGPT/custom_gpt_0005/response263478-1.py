
def foo(row, func, **kwargs):
    # Extract arguments from row based on kwargs
    args = {k: row[v] for k, v in kwargs.items() if v < len(row)}
    return func(**args)

# Example functions
def func1(a, b):
    return a + b

def func2(x, y, static=0):
    return x * y + static

# Sample data
row = [10, 20, 30, 40]

# Call the foo function with specific elements from the row
print(foo(row, func1, a=0, b=1))  # Outputs: 30 (10 + 20)
print(foo(row, func2, x=1, y=2, static=5))  # Outputs: 65 (20 * 30 + 5)
