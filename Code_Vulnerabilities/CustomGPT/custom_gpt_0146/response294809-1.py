
import numpy as np
import itertools

# Sample input data
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
    for key, value in item.items():
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Create formula lists
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Calculate the formula for the current item
    current_formula = []
    for a, b, c in zip(la, lb, lc):
        current_formula.append((a**2) + 2*b*c)

    formula.append(np.array(current_formula))

# Update the list_of_data dictionaries with the formula
for k in range(len(list_of_data)):
    result = {'formula': formula[k]}
    list_of_data[k].update(result)

# Output the final results
print("formula =", formula)
for data in list_of_data:
    print(data)
