
# List assignment
[a, b] = [1, 2]
print("List Assignment:")
print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2

# Tuple assignment
a, b = [3, 4]
print("\nTuple Assignment:")
print("a:", a)  # Output: a: 3
print("b:", b)  # Output: b: 4

# Demonstrating mutability
list_example = [a, b]
list_example[0] = 99
print("\nModified List Example:")
print("Updated list_example:", list_example)  # Output: Updated list_example: [99, 4]

# Tuples instance to show immutability
tuple_example = (a, b)
# The following line would raise an error if uncommented:
# tuple_example[0] = 100  # TypeError: 'tuple' object does not support item assignment
