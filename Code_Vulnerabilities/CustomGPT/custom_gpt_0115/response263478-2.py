
def func1(a, b):
    return a + b

def func2(a, c, d):
    return f"{a} combined with {c}, and {d}"

def func3(static_arg):
    return f"Static argument: {static_arg}"

# Example row
row = [10, 20, 30, 40]

# Using foo
result1 = foo(row, func1, row_indices=[0, 1])  # Takes row[0] and row[1]
result2 = foo(row, func2, row_indices=[0, 2], "extra_arg", d=row[3])
result3 = foo(row, func3, static_arg="Hello!")

print(result1)  # Output: 30
print(result2)  # Output: "10 combined with 30, and 40"
print(result3)  # Output: "Static argument: Hello!"
