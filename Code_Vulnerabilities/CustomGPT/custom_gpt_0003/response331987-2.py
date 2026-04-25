
# Tuple assignment
(a, b) = (1, 2)
print(a)  # Output: 1
print(b)  # Output: 2

# Attempting to modify a tuple
my_tuple = (1, 2)
try:
    my_tuple[0] = 3  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Output: 'tuple' object does not support item assignment
