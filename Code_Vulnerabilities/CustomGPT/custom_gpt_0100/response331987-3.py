
# List assignment
my_list = [1, 2, 3]
a, b = my_list
print(a, b)  # Output: 1 2

my_list[0] = 100  # Changing the first item in the list
print(my_list)  # Output: [100, 2, 3]

# Tuple assignment
my_tuple = (1, 2, 3)
c, d = my_tuple
print(c, d)  # Output: 1 2

# The following line would raise an error because tuples are immutable
# my_tuple[0] = 100
