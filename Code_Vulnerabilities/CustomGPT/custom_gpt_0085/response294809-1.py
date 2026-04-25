
import numpy as np
import itertools

# Sample data setup
list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Calculate formula
formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    current_formula = []
    for a, b, c in zip(la, lb, lc):
        current_formula.append((a**2) + 2*b*c)
    formula.append(current_formula)

# Update list_of_data with the new formula
for i in range(len(list_of_data)):
    result = {'formula': np.array(formula[i])}
    list_of_data[i].update(result)

# Output the results
print("Formula:", formula)
print("List of Data:", list_of_data)
