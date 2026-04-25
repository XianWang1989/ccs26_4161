
import itertools
import numpy as np

# Sample list of dictionaries with NumPy arrays
list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Prepare a variable to hold the new formulas for each entry
list_of_formulas = []

# Loop through each item in the list_of_data
for item in list_of_data:
    # Extract values from each dictionary
    la = item['a']
    lb = item['b']
    lc = item['c']

    # Calculate formulas for the corresponding arrays
    formula = [(a**2) + 2*b*c for a, b, c in zip(la, lb, lc)]

    # Append the result as an array to the list_of_formulas
    list_of_formulas.append(np.array(formula))

# Update each dictionary with the new formula
for i in range(len(list_of_data)):
    list_of_data[i]['formula'] = list_of_formulas[i]

# Display the updated list_of_data
print(list_of_data)
