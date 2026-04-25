
# List assignment
list_example = [1, 2, 3]
[a, b] = list_example
list_example[0] = 10  # Lists are mutable
print(a, b)          # Output: 1 2
print(list_example)  # Output: [10, 2, 3]

# Tuple assignment
tuple_example = (1, 2, 3)
x, y = tuple_example
# tuple_example[0] = 10  # This will raise an error because tuples are immutable
print(x, y)            # Output: 1 2
print(tuple_example)   # Output: (1, 2, 3)
