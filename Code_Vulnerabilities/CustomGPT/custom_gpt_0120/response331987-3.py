
# List Assignment
list_value = [1, 2]
[a, b] = list_value
list_value[0] = 3  # Modifying the list
print(a, b)      # Output: 1 2
print(list_value)  # Output: [3, 2]

# Tuple Assignment
tuple_value = (1, 2)  # Creating a tuple
a, b = tuple_value
# tuple_value[0] = 3  # This would raise an error
print(a, b)      # Output: 1 2
