
# List assignment
list_assignment = [1, 2]
a, b = list_assignment  # Unpacking the list
print("a (from list):", a)  # Output: a (from list): 1
print("b (from list):", b)  # Output: b (from list): 2

# Tuple assignment
tuple_assignment = (3, 4)
c, d = tuple_assignment  # Unpacking the tuple
print("c (from tuple):", c)  # Output: c (from tuple): 3
print("d (from tuple):", d)  # Output: d (from tuple): 4

# Mutability example
list_example = [5, 6]
list_example[0] = 100
print("Modified list:", list_example)  # Output: Modified list: [100, 6]

# Tuple example (will raise an error if you try to change it)
tuple_example = (7, 8)
# tuple_example[0] = 200  # This will raise a TypeError
