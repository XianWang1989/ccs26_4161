
# List assignment
[a, b] = [1, 2]
print("List Assignment:")
print(f"a: {a}, b: {b}")  # Output: a: 1, b: 2

# Tuple assignment
a, b = (3, 4)
print("\nTuple Assignment:")
print(f"a: {a}, b: {b}")  # Output: a: 3, b: 4

# Both can unpack from other iterables
a, b = [5, 6]
print("\nUnpacking from list:")
print(f"a: {a}, b: {b}")  # Output: a: 5, b: 6

a, b = (7, 8)
print("\nUnpacking from tuple:")
print(f"a: {a}, b: {b}")  # Output: a: 7, b: 8
