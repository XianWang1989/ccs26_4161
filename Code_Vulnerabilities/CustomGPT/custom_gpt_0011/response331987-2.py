
# Tuple assignment
(a, b) = (1, 2)

# Let's print the values
print("\nTuple Assignment:")
print("a =", a)
print("b =", b)

# Trying to modify a tuple (this would raise an error)
try:
    a_tuple = (1, 2)
    a_tuple[0] = 10  # This will cause a TypeError
except TypeError as e:
    print("Error occurred while trying to change a tuple:", e)
