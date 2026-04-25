
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
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist()) 
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize formula as an empty list
formula = []

for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]
    temp_formula = []  # Temporary list for each formula

    for a, b, c in zip(la, lb, lc):  # Use zip instead of itertools.izip
        temp_formula.append((a**2) + 2*b*c)

    formula.append(temp_formula)  # Append the list of formulas for each item

# Update the original list_of_data with the new formula arrays
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Create numpy array for the formula
    list_of_data[k].update(result)

# Outputs
print("formula =", formula)
print("list_of_data =", list_of_data)
