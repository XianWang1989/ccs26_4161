
import itertools
import numpy as np

# Initialize your input data
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

# Initialize a list to hold formula results
formula = []

for la, lb, lc in zip(list_of_a, list_of_b, list_of_c):
    result = [(a**2) + 2*b*c for a, b, c in zip(la, lb, lc)]
    formula.append(result)

# Update the original list_of_data with new formula entries
for i, item in enumerate(list_of_data):
    item['formula'] = np.array(formula[i])

# Output results
print("Formula:", formula)
print("List of Data:", list_of_data)
