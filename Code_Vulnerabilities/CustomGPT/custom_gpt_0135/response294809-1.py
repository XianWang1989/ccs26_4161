
import numpy as np
import itertools

list_of_data = [
    {'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
    {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
    {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}
]

# Prepare to hold lists of each component
list_of_a = []
list_of_b = []
list_of_c = []

# Populate lists with corresponding array values
for item in list_of_data:
    list_of_a.append(item['a'].tolist())
    list_of_b.append(item['b'].tolist())
    list_of_c.append(item['c'].tolist())

# Formula calculation and collection
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a temporary list for the current formula
    current_formula = []

    for a, b, c in zip(la, lb, lc):
        current_formula.append((a**2) + 2*b*c)

    # Append the current formula list to the main formula list
    formula.append(current_formula)

# Update the original dictionary with the new formulas
for k in range(len(list_of_data)):
    list_of_data[k]['formula'] = np.array(formula[k])

# Output Result
print("formula =", formula)
print("list_of_data =", list_of_data)
