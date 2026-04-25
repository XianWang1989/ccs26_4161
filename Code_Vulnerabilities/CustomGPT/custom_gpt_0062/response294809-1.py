
import numpy as np
import itertools

# Original list of dictionaries
list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Lists to hold values for each key
list_of_a = []
list_of_b = []
list_of_c = []

# Separate keys with corresponding values
for item in list_of_data:
    for key, value in item.items():  # Changed to items() for Python 3 compatibility
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Calculate formulas for each entry
formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):  # Changed to zip
    result = [(a ** 2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formula.append(result)

# Update dictionaries with the formula arrays
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])  # Store as numpy array

# Output the final result
print("formula =", formula)
print("list_of_data =", list_of_data)
