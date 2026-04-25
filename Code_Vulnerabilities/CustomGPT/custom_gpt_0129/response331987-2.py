
# Tuple assignment
a, b = [1, 2]
print(a)  # Output: 1
print(b)  # Output: 2

# Attempting to modify a tuple will raise an error
a_tuple = (1, 2)
try:
    a_tuple[0] = 99  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
