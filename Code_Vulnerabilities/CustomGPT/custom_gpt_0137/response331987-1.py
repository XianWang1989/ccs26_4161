
# List Assignment
[a, b] = [1, 2]
print("List Assignment: a =", a, "b =", b)  # Output: a = 1 b = 2

# Tuple Assignment
(a, b) = (1, 2)
print("Tuple Assignment: a =", a, "b =", b)  # Output: a = 1 b = 2

# Modifying a list
my_list = [1, 2, 3]
my_list[0] = 0  # Lists can be changed
print("Modified List:", my_list)  # Output: Modified List: [0, 2, 3]

# Attempting to modify a tuple (this will raise an error)
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 0  # This will raise an error
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment
