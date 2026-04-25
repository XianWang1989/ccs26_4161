
import itertools
import numpy as np  # Ensure to import numpy

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
    for key, value in item.items():  # Use items() instead of iteritems() in Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []  # To store lists of formulas
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create an empty container for the current formula list
    current_formula = []
    for a, b, c in zip(la, lb, lc):  # Use zip() instead of itertools.izip()
        current_formula.append((a ** 2) + 2 * b * c)

    # Append the current formula to the formula list
    formula.append(current_formula)

# Update each dictionary in list_of_data with the corresponding formula array
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Convert to numpy array
    list_of_data[k].update(result)

# Result Output
print("Formula:", formula)
print("List of Data:", list_of_data)
