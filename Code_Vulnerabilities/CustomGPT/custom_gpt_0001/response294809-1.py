
import numpy as np
import itertools

list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])}, 
                 {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                 {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize formula as a list of lists
formula = []
for i, val in enumerate(list_of_a):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a temporary list for the current formula
    temp_formula = []

    for a, b, c in zip(la, lb, lc):
        temp_formula.append((a**2) + 2*b*c)

    # Append the temporary list to the main formula list
    formula.append(temp_formula)

# Update list_of_data with the new formula arrays
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}
    list_of_data[k].update(result)

# For testing purposes, print the outputs
print("Formula:", formula)
print("List of Data:", list_of_data)
