
import itertools
import numpy as np  # Make sure to import numpy for array handling

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Store results for the formula
formula = []

for item in list_of_data:
    la = item['a']
    lb = item['b']
    lc = item['c']

    # Compute the formula for the current dictionary
    current_formula = [(a ** 2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formula.append(current_formula)

# Update the list_of_data with the computed formulas
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# Print results
print("formula =", formula)
print("\nlist_of_data =", list_of_data)
