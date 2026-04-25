
# List Assignment
list_example = [1, 2]
[a, b] = list_example
list_example[0] = 10  # Modifying the list
print(a, b)  # Output: 1 2 (a and b are unchanged)

# Tuple Assignment
tuple_example = (1, 2)
[a, b] = tuple_example
# tuple_example[0] = 10  # This would raise an error since tuples are immutable
print(a, b)  # Output: 1 2
