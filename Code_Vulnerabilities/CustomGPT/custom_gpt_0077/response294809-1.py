
import itertools
import numpy as np  # Ensure to import numpy for array handling

# Original list of data
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
    # Create a temporary list to hold formula results for each dictionary
    temp_formula = []
    for a, b, c in zip(la, lb, lc):
        temp_formula.append((a**2) + 2*b*c)
    formula.append(temp_formula)

# Update list_of_data with formula arrays
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])

# Display results
print("Formula:", formula)
print("List of Data:", list_of_data)
