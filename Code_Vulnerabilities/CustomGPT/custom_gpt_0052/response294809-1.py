
import numpy as np
import itertools

# Sample data
list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Initialize lists for each component
list_of_a = []
list_of_b = []
list_of_c = []

# Extract values into separate lists
for item in list_of_data:
    list_of_a.append(item['a'].tolist())
    list_of_b.append(item['b'].tolist())
    list_of_c.append(item['c'].tolist())

# Initialize formula list to store arrays
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Compute the formula and append as a numpy array
    result = [(a**2) + 2*b*c for a, b, c in zip(la, lb, lc)]
    formula.append(np.array(result))

# Update original list_of_data with new formulas
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = formula[k]

# Output the results
print("formula =", formula)
print("list_of_data =", list_of_data)
