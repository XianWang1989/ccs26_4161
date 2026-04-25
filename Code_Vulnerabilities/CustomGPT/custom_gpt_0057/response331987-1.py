
# List Assignment
[a, b] = [1, 2]
print(f"List Assignment: a = {a}, b = {b}")

# Tuple Assignment
a, b = [3, 4]
print(f"Tuple Assignment: a = {a}, b = {b}")

# Demonstrating mutability
list_example = [5, 6]
list_example[0] = 10
print(f"Modified List: {list_example}")

# Demonstrating immutability of tuples
tuple_example = (7, 8)
try:
    tuple_example[0] = 10
except TypeError as e:
    print(f"Error while modifying tuple: {e}")
