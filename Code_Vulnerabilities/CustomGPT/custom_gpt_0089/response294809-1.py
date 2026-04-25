
import numpy as np
import itertools

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
    for key, value in item.items():  # Use .items() instead of .iteritems()
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):  # Use zip directly
    formula_row = []  # Create a list to hold the results for this row
    for a, b, c in zip(la, lb, lc):
        formula_row.append((a**2) + 2*b*c)  # Compute for each element
    formula.append(formula_row)  # Append the row of results to formula

# Update list_of_data with the new 'formula' entry
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Use np.array to create an array
    list_of_data[k].update(result)

# Output the results
print("formula =", formula)
print("list_of_data =", list_of_data)
