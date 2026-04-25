
# List assignment
my_list = [1, 2]
[a, b] = my_list
my_list[0] = 99  # Changing the list
print(a, b)  # Output: 1 2 (unchanged)

# Tuple assignment
(a, b) = (1, 2)
# a and b remain constant since tuples are immutable
print(a, b)  # Output: 1 2
