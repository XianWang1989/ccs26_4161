
# List Assignment
my_list = [1, 2]
[a, b] = my_list
print(a, b)  # Output: 1 2

# Modifying list
my_list[0] = 99
print(my_list)  # Output: [99, 2]

# Tuple Assignment
(a, b) = (1, 2)
print(a, b)  # Output: 1 2

# Attempting to change a tuple will raise an error
# my_tuple = (1, 2)
# my_tuple[0] = 99  # This will raise TypeError: 'tuple' object does not support item assignment
