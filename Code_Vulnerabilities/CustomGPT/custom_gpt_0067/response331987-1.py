
# List assignment
list_assignment = [1, 2]
a, b = list_assignment
print("List Assignment:")
print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2

# Tuple assignment
tuple_assignment = (3, 4)
c, d = tuple_assignment
print("\nTuple Assignment:")
print("c:", c)  # Output: c: 3
print("d:", d)  # Output: d: 4

# Demonstrating mutability
list_example = [5, 6]
list_example[0] = 10  # This is valid
print("\nModified List:", list_example)  # Output: [10, 6]

# Demonstrating immutability
tuple_example = (7, 8)
# tuple_example[0] = 10  # This will raise a TypeError
