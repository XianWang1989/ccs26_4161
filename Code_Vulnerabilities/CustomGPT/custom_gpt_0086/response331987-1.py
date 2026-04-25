
# List assignment
[a, b] = [1, 2]
print("List assignment:", a, b)  # Output: 1 2

# Tuple assignment
a, b = (1, 2)
print("Tuple assignment:", a, b)  # Output: 1 2

# Changing values
list_example = [1, 2]
tuple_example = (1, 2)

# Modifying the list
list_example[0] = 10
print("Modified list:", list_example)  # Output: [10, 2]

# Trying to modify the tuple (will raise an error)
try:
    tuple_example[0] = 10
except TypeError as e:
    print("Error modifying tuple:", e)  # Raises TypeError
