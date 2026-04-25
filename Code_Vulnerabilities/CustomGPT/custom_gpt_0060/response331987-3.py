
# Example of list assignment
[a, b] = [1, 2]
print("List assignment:")
print(f"a = {a}, b = {b}")  # Output: a = 1, b = 2

# Example of tuple assignment using a list
a, b = [3, 4]
print("\nTuple assignment:")
print(f"a = {a}, b = {b}")  # Output: a = 3, b = 4

# Mutability check
list_assignment = [a, b]  # Here, list_assignment is a list
list_assignment[0] = 100
print("\nAfter altering list_assignment:")
print(list_assignment)  # Output: [100, 4]

# Tuple assignment inside a list (more explicitly)
(t1, t2) = (5, 6)  # This is a tuple assignment
print("\nTuple assignment explicitly:")
print(f"t1 = {t1}, t2 = {t2}")  # Output: t1 = 5, t2 = 6
