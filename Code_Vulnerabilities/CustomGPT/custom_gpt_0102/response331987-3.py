
# List assignment
[a, b] = [1, 2]
print(a, b)

# Tuple assignment
a, b = [3, 4]
print(a, b)

# Demonstrating with a function returning multiple values
def return_values():
    return 5, 6  # Returns a tuple

# Using tuple unpacking
x, y = return_values()
print(x, y)  # This works seamlessly with tuple unpacking
