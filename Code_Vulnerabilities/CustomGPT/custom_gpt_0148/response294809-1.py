
import itertools
import numpy as np

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

# Extract values for a, b, and c
for item in list_of_data:
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Calculate the formula
formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    # Calculate the formula result for each corresponding pair of values
    result = [(a**2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formula.append(result)

# Update list_of_data with new formula entries
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Create an array for the formula
    list_of_data[k].update(result)

# Output the results
print("formula =", formula)
print("list_of_data =", list_of_data)
