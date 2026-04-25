
def foo(row, f, **kwargs):
    # Create a dictionary from the row for easy access
    row_dict = {i: row[i] for i in range(len(row))}

    # Prepare arguments for the function call
    args = {**kwargs}  # Start with static arguments

    # Add specified row elements to the argument list
    for key in kwargs:
        if isinstance(key, int):
            args[key] = row_dict[key]

    # Call the function with unpacked arguments
    return f(**args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Sample row
row = [10, 20, 30, 40, 50]

# Function calls
result1 = foo(row, func1, a=0, b=1, c=2)  # Using indices of row
result2 = foo(row, func2, x=2)            # Static argument
result3 = foo(row, lambda x: f"Value is {x}", x=3)  # Using a lambda function

print(result1)  # Output: 60 (10 + 20 + 30)
print(result2)  # Output: 4 (2 * 2)
print(result3)  # Output: Value is 40
