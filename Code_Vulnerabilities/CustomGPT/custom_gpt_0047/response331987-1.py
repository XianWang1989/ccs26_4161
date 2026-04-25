
# List assignment
list_assignment = [1, 2]
a, b = list_assignment
print("List Assignment:")
print("a =", a)  # Output: 1
print("b =", b)  # Output: 2

# Tuple assignment
c, d = (3, 4)
print("\nTuple Assignment:")
print("c =", c)  # Output: 3
print("d =", d)  # Output: 4

# Demonstrating mutability of list
list_assignment[0] = 10
print("\nAfter modifying list_assignment:")
print("Modified List:", list_assignment)  # Output: [10, 2]
