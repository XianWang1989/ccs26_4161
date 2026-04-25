
import itertools
import numpy as np

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
    for key, value in item.items():  # Use .items() instead of .iteritems() in Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize an empty list for formulas
formula = []

# Compute formulas
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Store results for current entry in a temporary list
    current_formula = []
    for a, b, c in zip(la, lb, lc):  # Use zip instead of itertools.izip in Python 3
        current_formula.append((a**2) + 2*b*c)

    formula.append(current_formula)  # Append the current list of results

# Update the original list of data with formulas
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Convert list to numpy array
    list_of_data[k].update(result)

# Printing the results
print("formula =", formula)
print("list_of_data =", list_of_data)
