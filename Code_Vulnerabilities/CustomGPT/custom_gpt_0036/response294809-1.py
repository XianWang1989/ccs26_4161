
import itertools
import numpy as np

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Initialize the formula list
formula = []

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():  # Use .items() instead of .iteritems() (Python 3.x)
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Calculate the formula for each entry
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a list to hold the formulas for this entry
    entry_formula = []

    for a, b, c in zip(la, lb, lc):  # Use zip instead of itertools.izip() (Python 3.x)
        entry_formula.append((a**2) + 2 * b * c)

    # Append the formulated result as a list to the outer formula list
    formula.append(entry_formula)

# Update the original list_of_data with new formulas
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Use np.array to create numpy arrays
    list_of_data[k].update(result)

# Output the results
print("Formula:", formula)
print("List of Data:", list_of_data)
