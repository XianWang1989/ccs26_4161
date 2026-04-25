
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

# Initialize the formula list as a list of lists
formula = []
for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    # Create an array to hold the formula results for the current index
    current_formula = []
    for a, b, c in zip(la, lb, lc):
        current_formula.append((a**2) + 2*b*c)
    formula.append(current_formula)

# Update the original list_of_data with the new formula values
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Store the result as a numpy array
    list_of_data[k].update(result)

# Output the modified list_of_data and formula for verification
print("formula =", formula)
print("list_of_data =", list_of_data)
