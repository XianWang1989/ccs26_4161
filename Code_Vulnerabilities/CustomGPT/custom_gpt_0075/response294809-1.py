
import numpy as np
import itertools

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# To store lists of formulas
formula = []

for item in list_of_data:
    a = item['a']
    b = item['b']
    c = item['c']

    # Compute the formula
    result = (a**2) + 2 * b * c
    formula.append(result.tolist())

# Update each dictionary with the corresponding formula
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])

# Print results
print("Formula:", formula)
print("Updated list_of_data:", list_of_data)
