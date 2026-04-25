
def foo(row, func, **kwargs):
    # Prepare arguments by merging row elements with the static keyword arguments
    args = {**kwargs}  # Start with static arguments
    for key, index in kwargs.items():
        if isinstance(index, int):
            args[key] = row[index]  # Fetch row element if index is provided
    return func(**args)  # Call the function with the prepared arguments

# Example functions
def func1(a, b):
    return a + b

def func2(x, static_value):
    return x * static_value

# Example row
row = [10, 20, 30, 40]

# Usage of foo
result1 = foo(row, func1, a=0, b=1)  # Pass elements: row[0] and row[1]
result2 = foo(row, func2, x=2, static_value=5)  # Pass 2 (not from row) and static_value

print(result1)  # Output: 30
print(result2)  # Output: 10
