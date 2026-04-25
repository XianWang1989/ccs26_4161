
def func1(a, b, c):
    return a + b + c

def func2(x, y=1):
    return x * y

def func3(*args):
    return '-'.join(args)

# Example row (can be any type of data)
row = [10, 20, 30, 'spam', 'eggs']

# Example function calls
result1 = foo(row, func1, 0, 2)  # Using elements at index 0 and 2
result2 = foo(row, func2, 1, 3)  # Using element at index 1 and providing static argument
result3 = foo(row, func3, 3, 4)  # Using elements 3 and 4

print(result1)  # Output: 60 (10 + 30 + 20)
print(result2)  # Output: 20 (20 * 1)
print(result3)  # Output: spam-eggs
