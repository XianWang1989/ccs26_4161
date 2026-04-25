
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

for item in list_of_data:
    for key, value in item.items():  # Use items() for Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    formula_entry = [(a**2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formula.append(formula_entry)

# Update each dictionary with the new formula list
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# Print the results
print("formula =", formula)
print("list_of_data =", list_of_data)
