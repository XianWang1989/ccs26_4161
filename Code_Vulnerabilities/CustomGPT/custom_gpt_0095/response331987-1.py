
# List Assignment
list_assignment = [a, b] = [1, 2]
a += 1  # This modifies 'a'
print(a, b)  # Output: 2 2
print(list_assignment)  # Output: [2, 2]

# Tuple Assignment
a, b = (1, 2)  # This assigns the values 1 and 2 to a and b
a += 1  # This modifies 'a'
print(a, b)  # Output: 2 2
# Note: Tuple (1, 2) itself cannot be changed post assignment
