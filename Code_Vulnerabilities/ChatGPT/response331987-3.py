
# List assignment
list_values = [10, 20]
[a, b] = list_values
print("List assignment:")
print("a:", a)  # Output: a: 10
print("b:", b)  # Output: b: 20

# Tuple assignment
tuple_values = [30, 40]
x, y = tuple_values
print("\nTuple assignment:")
print("x:", x)  # Output: x: 30
print("y:", y)  # Output: y: 40

# Additional demonstration of mutability
list1 = [1, 2, 3]
[a, b] = list1
list1[0] = 99  # Changing the original list
print("\nAfter modifying original list:")
print("a:", a)  # Output: a: 1 (unchanged)
print("b:", b)  # Output: b: 2 (unchanged)
