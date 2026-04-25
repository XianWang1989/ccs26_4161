
# List assignment
list_example = [1, 2, 3]
[a, b] = list_example
print("List Assignment:")
print("a:", a)  # Output: 1
print("b:", b)  # Output: 2

# Modifying the list
list_example[0] = 10
print("Modified List:", list_example)  # Output: [10, 2, 3]

# Tuple assignment
tuple_example = (1, 2, 3)
a, b = tuple_example
print("\nTuple Assignment:")
print("a:", a)  # Output: 1
print("b:", b)  # Output: 2

# Trying to modify the tuple will result in an error
# tuple_example[0] = 10  # Uncommenting this line raises a TypeError
