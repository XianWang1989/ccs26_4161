
# List assignment
my_list = [1, 2, 3]
[a, b, c] = my_list
print(a, b, c)  # Output: 1 2 3

# Tuple assignment
my_data = (4, 5, 6)
x, y, z = my_data
print(x, y, z)  # Output: 4 5 6

# Unpacking a return value (typically using tuple assignment)
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20
