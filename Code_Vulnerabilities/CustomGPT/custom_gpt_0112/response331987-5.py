
# List Assignment
my_list = [1, 2]
[a, b] = my_list
print("List Assignment:")
print("a:", a, "b:", b)
my_list[0] = 10
print("Modified List:", my_list)

# Tuple Assignment
my_tuple = (1, 2)
a, b = my_tuple
print("\nTuple Assignment:")
print("a:", a, "b:", b)

# Uncommenting the following line will raise an error
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
