
# List assignment
[a, b] = [1, 2]
print("List assignment:")
print("a =", a)  # Output: a = 1
print("b =", b)  # Output: b = 2

# Tuple assignment
a, b = (3, 4)
print("\nTuple assignment:")
print("a =", a)  # Output: a = 3
print("b =", b)  # Output: b = 4

# Immutable nature of tuples
try:
    a, b = (5, 6)
    a = 10  # This is valid because 'a' is a variable, not the tuple itself
    print("\nAfter mutation:")
    print("a =", a)  # Output: a = 10
except Exception as e:
    print("Error:", e)
