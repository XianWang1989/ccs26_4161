
import itertools
import numpy as np  # Make sure to import numpy for array creation

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

# Create the formula as lists
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    formula_list = []  # Current list to store formula results
    for a, b, c in zip(la, lb, lc):
        formula_list.append((a ** 2) + 2 * b * c)
    formula.append(formula_list)  # Append the list of formula results

# Update the original list_of_data with the new formula structure
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Store as a numpy array
    list_of_data[k].update(result)

# Print results
print("Formula:", formula)
print("List of Data:", list_of_data)
