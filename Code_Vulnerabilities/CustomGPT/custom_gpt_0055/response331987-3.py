
# List assignment with varying length
[x, y, *rest] = [1, 2, 3, 4, 5]
print(x)    # Output: 1
print(y)    # Output: 2
print(rest)  # Output: [3, 4, 5]

# Tuple assignment
a, b, *rest = (1, 2, 3, 4, 5)  # This will raise an error as it's not a proper tuple unpacking
