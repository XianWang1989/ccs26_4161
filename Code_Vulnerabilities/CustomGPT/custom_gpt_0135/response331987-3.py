
# List assignment example
list_a = [1, 2]
[a, b] = list_a
list_a[0] = 10  # Modifying the original list
print(a, b)     # Output: 1 2 (a and b remain unaffected)

# Tuple assignment example
tuple_a = (1, 2)
a, b = tuple_a
# tuple_a[0] = 10  # This would raise an error as tuples are immutable
print(a, b)      # Output: 1 2
