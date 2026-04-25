
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

formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    local_formula = []
    for a, b, c in zip(la, lb, lc):
        local_formula.append((a**2) + 2*b*c)
    formula.append(np.array(local_formula))

# Update the dictionaries with the new formula lists
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = formula[k]

# Displaying the results
print("formula =", formula)
print("list_of_data =", list_of_data)
