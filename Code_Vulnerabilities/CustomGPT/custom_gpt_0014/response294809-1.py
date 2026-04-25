
import numpy as np
import itertools

list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
                 {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                 {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

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
    # Calculate the formula as a list
    calculations = [(a**2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formula.append(calculations)

# Update list_of_data with the new formula
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# Output results
print("formula =", formula)
print("list_of_data =", list_of_data)
