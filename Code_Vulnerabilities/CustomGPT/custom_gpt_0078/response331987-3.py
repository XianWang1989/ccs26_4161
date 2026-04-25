
# List assignment
[a, b] = [1, 2]
print(f"List Assignment: a = {a}, b = {b}")

# Tuple assignment
c, d = [3, 4]
print(f"Tuple Assignment: c = {c}, d = {d}")

# Trying to modify the elements in a list (mutable)
my_list = [1, 2, 3]
my_list[0] = 10   # Mutable
print(f"Modified List: {my_list}")

# Trying to modify a tuple (immutable)
my_tuple = (1, 2, 3)
# This will raise an error if uncommented
# my_tuple[0] = 10  
