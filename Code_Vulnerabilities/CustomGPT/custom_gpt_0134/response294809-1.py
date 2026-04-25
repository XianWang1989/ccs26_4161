
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
    list_of_a.append(item['a'].tolist())
    list_of_b.append(item['b'].tolist())
    list_of_c.append(item['c'].tolist())

formula = []
for i, va in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a new list for each formula group
    result_formula = []
    for a, b, c in zip(la, lb, lc):
        result_formula.append((a ** 2) + 2 * b * c)

    # Append the calculated group formula to the main formula list
    formula.append(result_formula)

# Update list_of_data with the new formula entries
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# Output the results
print("formula =", formula)
print("list_of_data =", list_of_data)
