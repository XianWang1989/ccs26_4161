
import numpy as np
import itertools

# Initialize input data
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

# Initialize the formula list
formula = []

for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Calculate the formula for each pair of items
    formula_values = []
    for a, b, c in zip(la, lb, lc):  # Use zip for Python 3
        formula_values.append((a**2) + 2*b*c)

    # Append the calculated formula values as an array
    formula.append(np.array(formula_values))

# Update list_of_data with the new formula
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = formula[k]

# Output the results
print("Formula:", formula)
print("List of Data:", list_of_data)
