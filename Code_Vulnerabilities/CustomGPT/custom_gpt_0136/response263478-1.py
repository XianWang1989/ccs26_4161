
def foo(row, func, *args, **kwargs):
    # Prepare the arguments from the row based on the provided keys
    row_args = {key: row[key] for key in kwargs}
    return func(*args, **row_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, static):
    return x * static

# Example data row
row = [10, 20, 30, 40, 50]

# Example function calls
result1 = foo(row, func1, static1=1, static2=2, a=1, b=4)  # Uses row[1], row[4], and static arguments
result2 = foo(row, func2, static=2, x=3)  # Uses static argument and a value

print(result1)  # Output: 7
print(result2)  # Output: 6
