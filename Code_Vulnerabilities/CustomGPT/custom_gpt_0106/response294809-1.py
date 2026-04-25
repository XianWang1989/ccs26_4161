
import itertools
import numpy as np  # Make sure to import numpy for array handling

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
    for key, value in item.items():  # Use items() for Python 3
        if key == 'a':
            list_of_a.append(value.tolist())
        elif key == 'b':
            list_of_b.append(value.tolist())
        elif key == 'c':
            list_of_c.append(value.tolist())

# Create a nested formula list where each entry corresponds to a row of calculations
formula = []
for i in range(len(list_of_a)):
    la = list_of_a[i]
    lb = list_of_b[i]
    lc = list_of_c[i]

    # Calculate values based on pairs of a, b, c
    f_values = []  # Temporarily store formula results for this entry
    for a, b, c in zip(la, lb, lc):
        f_values.append((a**2) + 2*b*c)

    formula.append(f_values)  # Append the calculated values as a new list

# Update the original list_of_data with the new formula list
for k in range(len(list_of_data)):
    result = {'formula': np.array(formula[k])}  # Store as a numpy array
    list_of_data[k].update(result)

# Output the results
print("formula =", formula)
print(list_of_data)
