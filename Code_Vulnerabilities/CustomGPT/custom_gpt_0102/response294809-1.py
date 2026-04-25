
import numpy as np
import itertools

# Define the initial list of data
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
    list_of_a.append(item['a'])
    list_of_b.append(item['b'])
    list_of_c.append(item['c'])

# Create a list to hold formula results for each entry
formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    formula_entry = []  # To hold the formula values for each entry
    for a, b, c in zip(la, lb, lc):
        formula_entry.append((a**2) + 2 * b * c)
    formula.append(formula_entry)  # Append the list of results for this entry

# Update the original list of dictionaries
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Use NumPy array for stored formula
    list_of_data[k].update(result)

# Display the resulting structures
print("Formula:", formula)
print("List of Data:", list_of_data)
