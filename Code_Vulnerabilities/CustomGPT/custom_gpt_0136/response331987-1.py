
# List Assignment
list_assignment = [0, 0]
list_assignment[0], list_assignment[1] = [1, 2]
print(list_assignment)  # Output: [1, 2]
list_assignment[0] = 10  # Modifying the list
print(list_assignment)  # Output: [10, 2]

# Tuple Assignment
tuple_assignment = (0, 0)
tuple_assignment = (1, 2)  # Reassigning the whole tuple
print(tuple_assignment)  # Output: (1, 2)
# tuple_assignment[0] = 10  # This will raise an error: TypeError: 'tuple' object does not support item assignment
