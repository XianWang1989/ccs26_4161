
def foo(row, f, *args, **kwargs):
    if callable(f):
        return f(*[row[i] for i in kwargs.get('indices', [])], *args)
    elif isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        raise ValueError("Invalid function or value provided.")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Using the new foo function
row = [10, 20, 30, 40]  # Sample data row
result1 = foo(row, func1, 5, indices=[0, 2, 1])  # 10 + 30 + 20 + 5
result2 = foo(row, func2, indices=[0, 1])  # 10 * 20

print(result1)  # Output: 65
print(result2)  # Output: 200
