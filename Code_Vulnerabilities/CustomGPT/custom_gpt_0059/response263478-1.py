
def foo(row, func, **kwargs):
    # Extract row values based on given keys and combine with static arguments
    params = {**{k: row[i] for i, k in enumerate(kwargs.get('row_keys', []))}, **kwargs.get('static', {})}
    return func(**params)

# Example functions
def func1(a, b):
    return a + b

def func2(x, y, c):
    return x * y + c

# Example usage
row = [1, 2, 3, 4, 5]

# Calling foo with specific elements from row by their keys, plus static arguments
result1 = foo(row, func1, row_keys=[0, 1])                # Uses row[0] and row[1]
result2 = foo(row, func2, row_keys=[1, 2], static={'c': 10})  # Uses row[1], row[2] and static c = 10

print(result1)  # Output: 3 (1 + 2)
print(result2)  # Output: 16 (2 * 3 + 10)
