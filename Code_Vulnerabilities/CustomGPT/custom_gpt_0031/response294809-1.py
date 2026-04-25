
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
    list_of_a.append(item['a'].tolist())
    list_of_b.append(item['b'].tolist())
    list_of_c.append(item['c'].tolist())

formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    formula_entry = []  # Create a new list for each entry
    for a, b, c in zip(la, lb, lc):
        formula_entry.append((a ** 2) + 2 * b * c)  # Calculate for each element
    formula.append(formula_entry)  # Append the list of results

# Update list_of_data with the new formula lists
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])

# Output the results
print("Formula:", formula)
print("List of Data:", list_of_data)
