
import numpy as np
import itertools

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

# Calculate formulas
formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    formula_entry = (la**2) + 2 * lb * lc
    formula.append(formula_entry)

# Update the original list_of_data with the new formulas
for k in range(len(list_of_data)):
    result = {'formula': formula[k]}
    list_of_data[k].update(result)

# Output the results
print("formula =", formula)
print("list_of_data =", list_of_data)
