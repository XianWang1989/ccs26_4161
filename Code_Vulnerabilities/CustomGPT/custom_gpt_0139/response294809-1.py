
import itertools
import numpy as np  # Make sure to import numpy to use arrays

# Initial list_of_data setup
list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# New lists to collect a, b, and c values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize formula as a list of lists
formula = []

# Calculate the formula results for each dictionary in list_of_data
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    inner_formula = []
    for a, b, c in zip(la, lb, lc):  # Use built-in zip in Python 3 instead of izip
        inner_formula.append((a**2) + 2*b*c)

    formula.append(inner_formula)  # Append the list for the current dictionary

# Update the original dictionaries with the new 'formula' key
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Convert to numpy array before updating
    list_of_data[k].update(result)

# Result check
print("formula =", formula)
print("list_of_data =", list_of_data)
