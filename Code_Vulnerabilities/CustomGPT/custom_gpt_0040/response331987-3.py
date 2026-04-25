
# List Assignment
[a, b] = [1, 2]
print(f"List Assignment: a = {a}, b = {b}")
# Changing the list
lst = [3, 4]
[a, b] = lst
print(f"Changed List Assignment: a = {a}, b = {b}")

# Tuple Assignment
a, b = (1, 2)
print(f"Tuple Assignment: a = {a}, b = {b}")
# Attempting to change tuple (will raise an error if you try to do it)
try:
    a, b = (3, 4)
except TypeError as e:
    print(f"Error: {e}")
