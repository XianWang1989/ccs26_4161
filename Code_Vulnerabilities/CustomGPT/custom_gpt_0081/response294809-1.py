
import itertools
import numpy as np  # Ensure numpy is imported for array creation

list_of_data = [{'a': np.array([1, 2]), 'b': np.array([3, 4]), 'c': np.array([5, 6])},
                 {'a': np.array([7, 8]), 'b': np.array([9, 10]), 'c': np.array([1, 2])},
                 {'a': np.array([-1, 4]), 'b': np.array([1, 10]), 'c': np.array([4, 5])}]

# Separate keys with corresponding values
list_of_a = []
list_of_b = []
list_of_c = []

for item in list_of_data:
    for key, value in item.items():  # Use .items() instead of .iteritems()
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Initialize list of lists for formula results
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Create a new list for the results corresponding to current set
    individual_formula = []
    for a, b, c in zip(la, lb, lc):  # Use zip instead of itertools.izip
        individual_formula.append((a ** 2) + 2 * b * c)

    # Append the individual_formula list to the main formula list
    formula.append(individual_formula)

# Update each dictionary in list_of_data with the corresponding formula
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Store formula as a numpy array
    list_of_data[k].update(result)

# Output results
print("formula =", formula)
print("list_of_data =", list_of_data)
