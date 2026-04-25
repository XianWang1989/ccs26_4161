
import numpy as np
import itertools

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Prepare lists for keys
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():  # Use items() instead of iteritems()
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Calculate formulas
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create an intermediate list to store results for the current dictionary
    pair_formula = []

    for a, b, c in zip(la, lb, lc):  # Use zip() instead of itertools.izip() in Python 3
        pair_formula.append((a**2) + 2 * b * c)

    # Append the list of formulas as array
    formula.append(np.array(pair_formula))  # Convert list to array before appending

# Update the original list_of_data with the new formula entries
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = formula[k]  # Assign the array directly

# Now formula should be a list of arrays
print("Formula =", formula)
print("List of data =", list_of_data)
