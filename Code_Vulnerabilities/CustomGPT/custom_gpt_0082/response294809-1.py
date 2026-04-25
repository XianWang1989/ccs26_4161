
import numpy as np
import itertools

# Initial list of dictionaries
list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Lists to hold values
list_of_a = []
list_of_b = []
list_of_c = []

# Separate keys with corresponding values
for item in list_of_data:
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []

# Calculate the formula for each pair of lists
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Calculate formula values
    formula_values = [(a**2) + 2 * b * c for a, b, c in zip(la, lb, lc)]
    formula.append(formula_values)

# Update the original dictionaries with the new formula
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# Output results
print("formula =", formula)
print("list_of_data =", list_of_data)
