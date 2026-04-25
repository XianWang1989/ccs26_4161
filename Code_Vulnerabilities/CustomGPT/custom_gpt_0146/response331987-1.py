
# List Assignment
list_a, list_b = [1, 2]
print("List Assignment:")
print("list_a:", list_a)  # Output: 1
print("list_b:", list_b)  # Output: 2

# Modifying the list
list_a = 10
print("After modifying list_a:", list_a)  # Output: 10
# Note that assigning a new value replaces the reference for list_a.

# Tuple Assignment
tuple_a, tuple_b = 3, 4
print("\nTuple Assignment:")
print("tuple_a:", tuple_a)  # Output: 3
print("tuple_b:", tuple_b)  # Output: 4

# Attempting to modify a tuple (this will raise an error)
try:
    tuple_a[0] = 100  # This will cause a TypeError
except TypeError as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment
