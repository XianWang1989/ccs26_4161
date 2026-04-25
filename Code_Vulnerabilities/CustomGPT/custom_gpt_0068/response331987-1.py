
# List assignment
[a, b] = [1, 2]
print("List Assignment:")
print(f"a: {a}, b: {b}")

# Demonstrating mutability of lists
list_example = [1, 2, 3]
list_example[0] = 10  # Changing the first element
print("Modified List:", list_example)

# Tuple assignment (interpreted from variable assignment)
a, b = (3, 4)
print("\nTuple Assignment:")
print(f"a: {a}, b: {b}")

# Attempting to change a tuple (will raise an error)
tuple_example = (1, 2, 3)
try:
    tuple_example[0] = 10  
except TypeError as e:
    print("Error trying to modify tuple:", e)
