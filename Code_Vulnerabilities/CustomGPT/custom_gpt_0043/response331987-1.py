
# List assignment
list_value = [1, 2]
[a, b] = list_value
print("List assignment:")
print(f"a = {a}, b = {b}")  # Outputs: a = 1, b = 2

# Tuple assignment
tuple_value = (1, 2)
a, b = tuple_value
print("\nTuple assignment:")
print(f"a = {a}, b = {b}")  # Outputs: a = 1, b = 2

# Demonstrating mutability of lists vs immutability of tuples
# Modifying the list
list_value[0] = 10
print("\nModified list:")
print(f"list_value = {list_value}")  # Outputs: list_value = [10, 2]

# Attempting to modify tuple will raise an error
try:
    tuple_value[0] = 10
except TypeError as e:
    print("\nAttempting to modify a tuple raises an error:")
    print(e)  # Outputs an error message
