
import numpy as np
import itertools

# Initial list of dictionaries
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
    list_of_a.append(item['a'])
    list_of_b.append(item['b'])
    list_of_c.append(item['c'])

# Create the formula
formulas = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    formula = [(a**2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formulas.append(formula)

# Update the list of dictionaries
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formulas[k])

# Output the results
print("Formula:", formulas)
print("List of Data:", list_of_data)
