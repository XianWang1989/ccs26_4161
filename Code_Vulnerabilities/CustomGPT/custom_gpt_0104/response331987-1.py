
# List assignment
list_assignment = [1, 2]
[a, b] = list_assignment
print("List Assignment:")
print("a =", a)  # Output: a = 1
print("b =", b)  # Output: b = 2

# Tuple assignment
tuple_assignment = [1, 2]  # Here using a list on the right side but unpacking into variables
a, b = tuple_assignment
print("\nTuple Assignment:")
print("a =", a)  # Output: a = 1
print("b =", b)  # Output: b = 2

# Modifying the list
list_assignment[0] = 10
print("\nModified List Assignment:")
print("list_assignment =", list_assignment)  # Output: list_assignment = [10, 2]
