
# List assignment
list_assignment = [1, 2]
[a, b] = list_assignment
print(a, b)  # Output: 1 2

# Tuple assignment
tuple_assignment = (1, 2)
c, d = tuple_assignment
print(c, d)  # Output: 1 2

# Assigning from a list using tuple unpacking
e, f = [3, 4]
print(e, f)  # Output: 3 4

# Note on mutability
example_list = [1, 2, 3]
example_tuple = (1, 2, 3)

# Modifying list
example_list[0] = 10
print(example_list)  # Output: [10, 2, 3]

# Trying to modify tuple (will raise an error)
# example_tuple[0] = 10  # Uncommenting this will cause a TypeError
