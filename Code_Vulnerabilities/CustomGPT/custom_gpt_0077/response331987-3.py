
# List assignment
list_data = [3, 4]
[a, b] = list_data
print(a, b)  # Output: 3 4

# Tuple assignment
tuple_data = (5, 6)
c, d = tuple_data
print(c, d)  # Output: 5 6

# Using a function that returns multiple values
def get_coordinates():
    return (7, 8)

x, y = get_coordinates()
print(x, y)  # Output: 7 8
