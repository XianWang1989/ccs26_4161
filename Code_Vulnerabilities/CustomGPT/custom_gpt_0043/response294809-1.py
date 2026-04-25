
import itertools
import numpy as np

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Create separated lists for keys 'a', 'b', 'c'
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

# List to hold formulas
formula = []

for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Temporary list to hold the formulas for each entry
    temp_formula = []

    for a, b, c in zip(la, lb, lc):  # Change izip to zip in Python 3
        temp_formula.append((a ** 2) + 2 * b * c)

    formula.append(temp_formula)  # Add the list of formulas to the main list

# Update list_of_data with the new structure
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Convert to numpy array
    list_of_data[k].update(result)

# For demonstration purposes, print the results
print("formula =", formula)
print("list_of_data =", list_of_data)
